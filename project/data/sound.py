from pygame import mixer


class Sound:
    def __init__(self, sound_file, volume=1):
        self.sound = mixer.Sound(sound_file)
        self.volume = float(volume)
        self.mod = 1

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        if volume > 1: volume = 1
        if volume < 0: volume = 0
        self.mod = volume
        self.sound.set_volume(self.volume*self.mod)

    def play(self):
        self.sound.set_volume(self.volume*self.mod)
        mixer.Sound.play(self.sound)


class MusicPlayer:
    def __init__(self, songs=[], delay=5):
        self.mixer = mixer
        self.channel = self.mixer.find_channel()
        self.songs = songs
        self.song_index = 0
        self.delay = delay*60
        self.timer = 0

    def play(self):
        if len(self.songs) == 0: return
        self.channel.play(self.songs[self.song_index].sound)

    def play_next_song(self):
        self.song_index += 1
        if self.song_index >= len(self.songs):
            self.song_index = 0

        self.play()

    def queue_next_song(self):
        self.song_index += 1
        if self.song_index >= len(self.songs):
            self.song_index = 0

        self.channel.queue(self.songs[self.song_index].sound)

    def update(self):
        if self.channel.get_busy(): return
        self.timer += 1
        if self.timer >= self.delay:
            self.play_next_song()
            self.timer = 0