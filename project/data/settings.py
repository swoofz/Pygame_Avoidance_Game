class Settings:
    def __init__(
        self, master_sound=1, sfx_sound=1, background_sound=1
    ):
        self.master = master_sound
        self.sfx = sfx_sound
        self.bg_sound = background_sound

    def set_master(self, volume):
        self.master = volume

    def set_sfx(self, volume):
        self.sfx = volume

    def set_background_volume(self, volume):
        self.bg_sound = volume

    def load(self, data):
        volume = data['volume']
        
        self.master = volume['master_volume']
        self.sfx = volume['sfx_volume']
        self.bg_sound = volume['background_volume']

    def save(self):
        return {
            "volume": {
                "master_volume": self.master,
                "sfx_volume": self.sfx,
                "background_volume": self.bg_sound
            }
        }