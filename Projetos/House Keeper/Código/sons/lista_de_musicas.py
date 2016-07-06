from sense_hat import SenseHat
sense = SenseHat
import pygame

def musicas ():
    while True:
        musicas = raw_input('escolha a sua musica:')
        if musicas == 'invencible':
                print ('tocando a musica selecionada')
                pygame.mixer.init()
                pygame.mixer.music.load("DEAF KEV - Invincible [NCS Release].mp3")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    continue
        elif musicas == 'dont let me down':
                print ('tocando a musica selecionada')
                pygame.mixer.init()
                pygame.mixer.music.load("The Chainsmokers - Dont Let Me Down (Illenium Remix).mp3")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    continue
        elif musicas == 'never forguet you':
                print ('tocando a musica selecionada')
                pygame.mixer.init()
                pygame.mixer.music.load("Zara Larsson - Never Forget You (Price & Takis Remix).mp3")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    continue
                
        elif musicas == 'stressed Out':
                print ('tocando a musica selecionada')
                pygame.mixer.init()
                pygame.mixer.music.load(".Twenty One Pilots - Stressed Out (Tomsize Remix)mp3")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    continue

        elif musicas == 'light it up':
            print ('tocando a musica selecionada')
            pygame.mixer.init()
            pygame.mixer.music.load("Major Lazer - Light It Up (Feat. NYLA & Fuse ODG) (YP Remix).mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue

        elif musicas == 'now that ive found you':
                print ('tocando a musica selecionada')
                pygame.mixer.init()
                pygame.mixer.music.load("Martin Garrix - 'Now That I've Found You (feat. John & Michel)' [Official Video].mp3")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    continue
        elif musicas == '7 years':
                print ('tocando a musica selecionada')
                pygame.mixer.init()
                pygame.mixer.music.load("Lukas Graham - 7 Years (T-Mass Remix) [feat. Toby Romeo].mp3")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    continue
        elif musicas == "back":
            musicas()
        else:
            print "erro"
            





musicas()

