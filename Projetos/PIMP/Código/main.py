#!/usr/bin/env python3
import sys
import os
import search
import download
import player
import speech
from PyQt5 import QtWidgets, QtCore
from gui import Ui_MainWindow
try:
    import sense_hat
    import icons
except ModuleNotFoundError:
    print('Couldn\'t import sense_hat')


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    signal_start_transcribing = QtCore.pyqtSignal()
    signal_start_searching = QtCore.pyqtSignal(str)
    signal_start_downloading = QtCore.pyqtSignal(str)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.ext = '.flac'

        self.playlist_file = 'playlist.txt'
        self.playlist = list()
        if os.path.isfile(self.playlist_file):
            with open(self.playlist_file, 'r') as file:
                for line in file.readlines():
                    self.playlist.append(line.strip())

        # 1 GiB
        self.cache_size = 1073741824

        while self.calculate_size() > self.cache_size:
            os.remove(self.oldest_file())

        if len(self.playlist) > 0:
            self.current_video_id = self.playlist[0]
        else:
            self.current_video_id = str()

        self.music_player = player.Player()
        try:
            self.sense_hat = sense_hat.SenseHat()
        except NameError:
            self.sense_hat = None

        self.downloader_thread = QtCore.QThread()
        self.downloader = Downloader(self)
        self.downloader.moveToThread(self.downloader_thread)
        self.signal_start_downloading.connect(self.downloader.download)
        self.downloader_thread.start()

        self.search_thread = QtCore.QThread()
        self.search = YoutubeSearch(self)
        self.search.moveToThread(self.search_thread)
        self.signal_start_searching.connect(self.search.search)
        self.search_thread.start()

        self.horizontalSlider.setValue(100)
        self.horizontalSlider.valueChanged.connect(self.update_volume)

        self.pushButton_close.clicked.connect(self.close)
        self.pushButton_mute.clicked.connect(self.media_mute)
        self.pushButton_play.clicked.connect(self.media_play)
        self.pushButton_pause.clicked.connect(self.media_pause)
        self.pushButton_stop.clicked.connect(self.media_stop)
        self.pushButton_search.clicked.connect(self.start_text)
        self.lineEdit.returnPressed.connect(self.start_text)
        self.pushButton_forwards.clicked.connect(self.media_forward)
        self.pushButton_back.clicked.connect(self.media_backward)

        if speech.found_module:
            self.voice_thread = QtCore.QThread()
            self.voice_recognition = VoiceRecognition(self)
            self.voice_recognition.moveToThread(self.voice_thread)
            self.signal_start_transcribing.connect(self.voice_recognition.transcribe)
            self.voice_thread.start()
            
            self.pushButton_voice.clicked.connect(self.start_voice)
        else:
            self.pushButton_voice.setEnabled(False)

        if self.sense_hat is not None:
            self.sense_hat.stick.direction_up = self.volume_up
            self.sense_hat.stick.direction_down = self.volume_down
            self.sense_hat.stick.direction_left = self.media_backward
            self.sense_hat.stick.direction_right = self.media_forward

    def search_download_and_play(self, search_terms):
        self.signal_start_searching.emit(search_terms)

    def start_text(self):
        self.search_download_and_play(self.lineEdit.text())

    def start_voice(self):
        self.signal_start_transcribing.emit()

    @QtCore.pyqtSlot(str)
    def start_voice_2(self, transcription):
        if transcription.lower() == 'pause':
            self.media_pause()
        elif transcription.lower() == 'play':
            self.media_play()
        elif transcription.lower() == 'stop':
            self.media_stop()
        elif transcription.lower() == 'forward' or transcription.lower() == 'forwards' \
                or transcription.lower() == 'next':
            self.media_forward()
        elif transcription.lower() == 'backward' or transcription.lower() == 'backwars' \
                or transcription.lower() == 'back' or transcription.lower() == 'previous':
            self.media_backward()
        else:
            self.search_download_and_play(transcription)

    def update_volume(self):
        volume = self.horizontalSlider.value() + 1
        self.music_player.set_volume(volume)
        self.label_volume.setText(str(volume) + '%')

        if self.sense_hat is not None:
            if volume < 33:
                self.sense_hat.set_pixels(icons.volume_min)
            elif volume < 66:
                self.sense_hat.set_pixels(icons.volume_med)
            else:
                self.sense_hat.set_pixels(icons.volume_max)

    def media_mute(self):
        self.music_player.mute()
        self.pushButton_mute.setText('Unmute')
        if self.sense_hat is not None:
            self.sense_hat.set_pixels(icons.mute)
        self.pushButton_mute.clicked.disconnect()
        self.pushButton_mute.clicked.connect(self.media_unmute)

    def media_unmute(self):
        self.music_player.unmute()
        self.pushButton_mute.setText('Mute')
        if self.sense_hat is not None:
            self.sense_hat.set_pixels(icons.play)
        self.pushButton_mute.clicked.disconnect()
        self.pushButton_mute.clicked.connect(self.media_mute)

    def media_play(self):
        self.music_player.play()
        self.label_status.setText('Playing')
        if self.sense_hat is not None:
            self.sense_hat.stick.direction_middle = self.media_pause
            self.sense_hat.set_pixels(icons.play)

    def media_pause(self):
        self.music_player.pause()
        self.label_status.setText('Paused')
        if self.sense_hat is not None:
            self.sense_hat.stick.direction_middle = self.media_play
            self.sense_hat.set_pixels(icons.pause)

    def media_stop(self):
        self.music_player.stop()
        self.label_status.setText('Stopped')

    def media_open(self, file):
        self.music_player.open(file)
        if not file.split(sep='.')[0] in self.playlist:
            self.add_to_playlist(file.split(sep='.')[0])

    def volume_up(self):
        volume = self.horizontalSlider.value() + 1
        self.horizontalSlider.setValue(volume + 10)

    def volume_down(self):
        volume = self.horizontalSlider.value() + 1
        self.horizontalSlider.setValue(volume - 10)

    def add_to_playlist(self, video_id):
        self.playlist.append(video_id)
        with open(self.playlist_file, 'a') as file:
            file.write(video_id + '\n')

    def media_forward(self):
        if len(self.playlist) > 0 and self.current_video_id != '':
            if self.sense_hat is not None:
                self.sense_hat.set_pixels(icons.forward)

            index = self.playlist.index(self.current_video_id)
            target_index = index + 1
            if target_index > len(self.playlist) - 1:
                target_index = len(self.playlist) - 1

            self.download_and_play(self.playlist[target_index])

    def media_backward(self):
        if len(self.playlist) > 0 and self.current_video_id != '':
            if self.sense_hat is not None:
                self.sense_hat.set_pixels(icons.backwards)

            index = self.playlist.index(self.current_video_id)
            target_index = index - 1
            if target_index < 0:
                target_index = 0

            self.download_and_play(self.playlist[target_index])

    @QtCore.pyqtSlot(str)
    def download_and_play(self, video_id):
        self.current_video_id = video_id
        if not os.path.isfile(self.current_video_id + self.ext):
            self.signal_start_downloading.emit(self.current_video_id)
        else:
            self.play_file()

    @QtCore.pyqtSlot()
    def play_file(self):
        self.media_open(self.current_video_id + self.ext)
        self.media_play()

    def calculate_size(self):
        total_size = 0
        for filename in os.listdir(os.getcwd()):
            if filename.endswith('.flac'):
                total_size += os.path.getsize(filename)
        return total_size

    def oldest_file(self):
        oldest_file = str()
        oldest_time = 0.0
        for filename in os.listdir(os.getcwd()):
            if filename.endswith('.flac'):
                if oldest_time == 0.0:
                    oldest_time = os.path.getmtime(filename)
                    oldest_file = filename
                else:
                    if os.path.getmtime(filename) < oldest_time:
                        oldest_time = os.path.getmtime(filename)
                        oldest_file = filename
        return oldest_file


class VoiceRecognition(QtCore.QObject):
    signal_finished_transcribing = QtCore.pyqtSignal(str)

    def __init__(self, main, parent=None):
        super(VoiceRecognition, self).__init__(parent)

        self.main = main

        self.signal_finished_transcribing.connect(self.main.start_voice_2)

    @QtCore.pyqtSlot()
    def transcribe(self):
        transcription = speech.transcribe()
        self.signal_finished_transcribing.emit(transcription)


class YoutubeSearch(QtCore.QObject):
    signal_finished_searching = QtCore.pyqtSignal(str)

    def __init__(self, main, parent=None):
        super(YoutubeSearch, self).__init__(parent)

        self.main = main

        self.signal_finished_searching.connect(self.main.download_and_play)

    @QtCore.pyqtSlot(str)
    def search(self, search_terms):
        video_id = search.search(search_terms)
        self.signal_finished_searching.emit(video_id)


class Downloader(QtCore.QObject):
    signal_finished_downloading = QtCore.pyqtSignal()

    def __init__(self, main, parent=None):
        super(Downloader, self).__init__(parent)

        self.main = main

        self.signal_finished_downloading.connect(self.main.play_file)

    @QtCore.pyqtSlot(str)
    def download(self, video_id):
        download.download(video_id)

        self.signal_finished_downloading.emit()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec_())
