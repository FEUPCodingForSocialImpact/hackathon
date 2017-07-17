import vlc


class Player:
    def __init__(self):
        self.player = vlc.MediaPlayer()
        self.instance = vlc.Instance()

    def open(self, file):
        self.player.set_media(self.instance.media_new_path(file))

    def play(self):
        self.player.play()

    def stop(self):
        self.player.stop()

    def pause(self):
        self.player.pause()

    def mute(self):
        self.player.audio_set_mute(True)

    def unmute(self):
        self.player.audio_set_mute(False)

    def set_volume(self, volume):
        self.player.audio_set_volume(volume)

    def ended(self):
        if self.player.get_state() == vlc.State.Ended:
            return True
        else:
            return False
