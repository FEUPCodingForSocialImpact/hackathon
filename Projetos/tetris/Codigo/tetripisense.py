"""
Jogo tipo Tetris com LEDs para o SenseHat

Controles (continuando com os mapeamentos de joystick para teclado do Sense Hat):
     Joystick para a esquerda / seta para a esquerda - mover para a esquerda
     Joystick direito / seta para a direita - mover para a direita
     Joystick up / Up Arrow - Girar no sentido horário
     Joystick Down / Down Arrow - Soltar bloco atual
     Joystick press / Return key - Não está atualmente configurado
    
--------------------------------------------------------------------------
"""

import sys, pygame, random, sense_hat, math, serial
from pygame.color import Color

print("Tetris")

PORT = "/dev/ttyACM0"
BAUD = 115200
mb = serial.Serial(PORT, timeout=0.15)
mb.baudrate = BAUD
mb.parity   = serial.PARITY_NONE
mb.databits = serial.EIGHTBITS
mb.stopbits = serial.STOPBITS_ONE

WIDTH = 8
WORKAREA_HEIGHT = 12  
WORKAREA_SIZE = WIDTH, WORKAREA_HEIGHT
ACTUAL_HEIGHT = 8  
ACTUAL_SIZE = WIDTH, ACTUAL_HEIGHT
TOTAL_LEDS = WIDTH * ACTUAL_HEIGHT
CLEAR = (0, 0, 0, 0)
THRESHOLD = 10 
FRAME_RATE = 10 
BASE_FRAMES = 10  
sense = sense_hat.SenseHat()

print("Tetris")

def sensehat_display(surface):
    """Transferir uma Superfície pygame para os LEDs do Sense Hat.

     Esta função constrói um buffer de quadro fb de valores (r, g, b) adequados para o
     Método de set_pixels do Hat. Isto é feito extraindo esses valores de
     valores de pygame (r, g, b, a), tratando o valor final como intensidade.
    """
    fb = []
    w, h = surface.get_size()
    for y in range(h):
        row = ""
        for x in range(w):
            r, g, b, a = surface.get_at((x, y))
            red = int(r * a / 255)
            green = int(g * a / 255)
            blue = int(b * a / 255)
            fb.append((red, green, blue))

    sense.set_pixels(fb[-TOTAL_LEDS:])


def blank_canvas(size=WORKAREA_SIZE):
    """configurar e retroceder o pygame.Surface com todos os pixels desligados"""
    p = pygame.Surface(size, pygame.SRCALPHA)
    p.fill(CLEAR)
    return p


def surface_from_pattern(pattern, colour):
    """
   Retroceder um objeto pygame.Surface de acordo com o padrão e a cor fornecidos.
     O padrão é uma lista de linhas, cada linha é uma lista de 1s e 0s.
    """
    height = len(pattern)  
    width = (max(len(row) for row in pattern))
    o = blank_canvas(size = ((width, height)))
    for y, row in enumerate(pattern):
        for x, element in enumerate(row):
            if element:
                o.set_at((x, y), colour)
    return o


def all_block_variants(pattern, colour):
    """
     Dado um padrão, crie o pygame.Surface correspondente para ele com
     surface_from_pattern() acima; também criar todos os seus possíveis
     variantes se giradas.
    """
    block_surface = surface_from_pattern(pattern, colour)
    pixels = sum(pixel for row in pattern for pixel in row)
    block_mask = pygame.mask.from_surface(block_surface, THRESHOLD)
    list_of_variants = [block_surface, ]
    for angle in (-90, -180, -270):  
        rotated_surface = pygame.transform.rotate(block_surface, angle)
        rotated_mask = pygame.mask.from_surface(rotated_surface, THRESHOLD)
        if block_mask.overlap_area(rotated_mask, (0, 0)) == pixels:
            break
        list_of_variants.append(rotated_surface)
    return list_of_variants


def blockdata_list():
    """
    Criar uma superficie para cada bloco assim como para as suas superficies, se sofrerem uma rotação,
    e colocar isto numa matriz. Dado um pequeno display, alguns blocos menores são usados.
    """
    bl = []
    bl.append(all_block_variants([[1, 1], [1, 1]], Color('magenta')))
    bl.append(all_block_variants([[0, 1], [1, 1], [1, 0]], Color('blue')))
    bl.append(all_block_variants([[1, 0], [1, 1], [0, 1]], Color('darkorange4')))
    bl.append(all_block_variants([[1, 1, 1], [0, 1, 0]], Color('red')))
    bl.append(all_block_variants([[1, 1], [1, 0], [1, 0]], Color('cyan')))
    bl.append(all_block_variants([[1, 1], [0, 1], [0, 1]], Color('salmon')))
    bl.append(all_block_variants([[1,], [1,], [1,]], Color('yellow')))
    return bl


def block_mask(block, x, y):
    """Retroceder a pygame.mask para o bloco específico e a respetiva posição"""
    block_canvas = blank_canvas()
    block_canvas.blit(block, [x, y], special_flags=pygame.BLEND_RGBA_ADD)
    return pygame.mask.from_surface(block_canvas, THRESHOLD)


def game_over(frames):
    """Mostrar a pontuação etc, sair de maneira fluída"""
    score = int(frames / 10)  
    print("Game over, score: {0}".format(score))
    canvas = blank_canvas(ACTUAL_SIZE)
    pygame.draw.line(canvas, Color('red'), (0, 0), (WIDTH - 1, ACTUAL_HEIGHT - 1))
    pygame.draw.line(canvas, Color('red'), (WIDTH - 1, 0), (0, ACTUAL_HEIGHT - 1))
    sensehat_display(canvas)
    pygame.time.wait(2000)
    sense.show_message("Score: " + str(score), text_colour=Color('navyblue')[:3])


class Block:
    """
    Classe para armazenar dados do bloco: Forma do bloco, variantes dessa forma quando
     dados úteis rotacionados e associados para permitir fácil acesso ao próximo
     variante se girado [clockise]. As variantes são pré-geradas
     o que significa que o trabalho para calcular as variantes rotacionadas não precisa
     acontecer durante o jogo - embora isso seja apenas uma preocupação teórica com
     o Pi tendo uma enorme quantidade de poder de processamento em comparação com o
     transformações para o número muito pequeno de pixels nas formas sendo
     computado.
    """
    blocks_data = blockdata_list()

    def __init__(self):
        """
        Criar um novo bloco (selecionar uma forma aleatoriamente) e preencher atributos relacionados como auto permutações, auto rotação etc.
        """
        self._block = self.blocks_data[random.randrange(0, len(self.blocks_data))]
        self.permutations = len(self._block)
        self.index = 0
        self.set_shape_attributes()

    @property
    def rotated_clockwise_index(self):
        return (self.index + 1) % self.permutations

    def set_shape_attributes(self):
        self.current_shape = self._block[self.index]
        self.rotated = self._block[self.rotated_clockwise_index]

    def rotate_clockwise(self):
        """Ajustar o bloco +  atributos relacionados com a rotação no sentido horario"""
        self.index = self.rotated_clockwise_index
        self.set_shape_attributes()


class MyPlayarea:
    """Manter o funcionamento do jogo, e tornar constante a queda dos blocos"""

    def __init__(self, size=WORKAREA_SIZE):
        pygame.init()  
        self.background = blank_canvas()  
        self.width = size[0]
        self.height = size[1]
        self.setup_new_block()

    def setup_new_block(self):
        block = Block()
        new_x = 3
        new_y = WORKAREA_HEIGHT - ACTUAL_HEIGHT - block.current_shape.get_height()
        if self.can_place_block_here(block.current_shape, new_x, new_y):
            self.block = block
            self.block_x = new_x
            self.block_y = new_y
            return True
        else:
            return False

    def can_place_block_here(self, block, x, y):
        """
       Verificar se o bloqueio em (x, y) ultrapassaria as bordas da área de trabalho.
       Verificar se não há colisão com o conteúdo existente da área de trabalho do bloco é colocado na posição (x, y).
        """
        border_violation = x < 0 or y < 0 or \
                           x + block.get_width() > self.width or \
                           y + block.get_height() > self.height
        background_mask = pygame.mask.from_surface(self.background, THRESHOLD)
        collision = background_mask.overlap(block_mask(block, x, y), (0, 0))
        return not (border_violation or collision)

    def block_move(self, dx, dy):
        """
        Verificar se existe espaço vazio disponível e também se o bloco que está atualmente em queda se move por (dx, dy) pixels 
        """
        if self.can_place_block_here(self.block.current_shape, self.block_x + dx,
                                     self.block_y + dy):
            self.block_x = self.block_x + dx
            self.block_y = self.block_y + dy
            return True
        else:
            return False

    def block_rotate(self):
        """
        Verificar se existe espaço vazio disponível e também se o bloco que está atualmente em queda realiza a rotação no sentido horário em 90 graus
    
        """
        if self.can_place_block_here(self.block.rotated, self.block_x, self.block_y):
            self.block.rotate_clockwise()
            return True
        else:  
            if self.can_place_block_here(self.block.rotated, self.block_x + 1, self.block_y):
                self.block.rotate_clockwise()
                return self.block_move(1, 0)  
            if self.can_place_block_here(self.block.rotated, self.block_x - 1, self.block_y):
                self.block.rotate_clockwise()
                return self.block_move(-1, 0)  
            return False

    def add_block_to_background(self):
        """
        Adicionar o atual bloco em queda à sua posição atual e orientação para o plano de fundo
        """
        self.background.blit(self.block.current_shape, [self.block_x, self.block_y],
                             special_flags=pygame.BLEND_RGBA_ADD)

    def render(self):
        '''Renderizar o fundo e a posição atual do bloco'''
        screen = blank_canvas()
        screen.blit(self.background, (0, 0))
        screen.blit(self.block.current_shape, [self.block_x, self.block_y],
                    special_flags=pygame.BLEND_RGBA_ADD)
        sensehat_display(screen)

    def remove_full_lines(self):
        """
        remover todas as linhas horizontais completas na área de trabalho; mover o conteúdo acima da linha para o espaço criado pela remoção da mesma.
        """
        background_mask = pygame.mask.from_surface(self.background, THRESHOLD)
        for row in range(self.height):
            check_area = blank_canvas()
            pygame.draw.line(check_area, Color('white'), (0, row), (self.width - 1, row))
            check_area_mask = pygame.mask.from_surface(check_area, THRESHOLD)
            if background_mask.overlap_area(check_area_mask, (0, 0)) == self.width:
                self.background.set_clip(pygame.Rect((0, 0), (self.width, row + 1)))
                self.background.scroll(0, 1)
                self.background.set_clip(None)
                background_mask = pygame.mask.from_surface(self.background, THRESHOLD)


def run_game():
    global mb
    sense.clear()
    pygame.init()

  
    pygame.display.set_mode((1, 1))
    mov = mb.readline().decode().rstrip()
    clock = pygame.time.Clock()
    s = MyPlayarea()
    frames = 0
    print("mov")
    frames_before_drop = BASE_FRAMES
    drop_block = False
    try:
        while True:
            frames += 8
            moved = False
            if drop_block and mov == "Up" or mov == "Down":
                    drop_block = False
            if not drop_block and not moved:
                mov = mb.readline().decode().rstrip()
                if mov == "Left":
                        moved = s.block_move(-1, 0)
                if mov == "Right":
                        moved = s.block_move(1, 0)
                if mov == "Up":
                        moved = s.block_rotate()
                if mov == "Down":
                        drop_block = True
            
            frames_before_drop -= 1
            if frames_before_drop == 0:
                if s.block_move(0, 1):
                    pass
                else:  
                    s.add_block_to_background()
                    s.remove_full_lines()
                    if not s.setup_new_block():
                        break  
                    drop_block = False
                frames_before_drop = BASE_FRAMES - int(math.log(frames, 5))
            s.render()
            if drop_block:
                clock.tick(FRAME_RATE * BASE_FRAMES)  
            else:
                clock.tick(FRAME_RATE)
    except KeyboardInterrupt:
        return
    game_over(frames)
    
    answer = mb.readline().decode().rstrip()
    while answer not in ('y', 'n'):
        answer = mb.readline().decode().rstrip()
    if answer == 'y':
        run_game()
    else:
        print('Goodbye')
        pygame.quit()

if __name__ == '__main__':
    run_game()
    sense.clear()
    pygame.quit()
