import json
from .const import pygame, MUSIC_PLAYER, SOUNDS
from .elements import CONTENT, SETTINGS, MASTER_SLIDER, MASTER_SLIDER_VALUE,SFX_SLIDER, SFX_SLIDER_VALUE, BG_SLIDER, BG_SLIDER_VALUE

def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

    return True

def run_game():
    while event_handler():
        CONTENT.display_window()
        MUSIC_PLAYER.update()
        pygame.display.update()

def setup():
    load_sound()
    MUSIC_PLAYER.play()



def load_sound():
    with open('./data/saves/settings.json', 'r') as f:
        data = json.load(f)

    SETTINGS.load(data)
    update_setting_sliders()
    for sound in SOUNDS["Background"]:
        new_volume = sound.get_volume() * SETTINGS.master * SETTINGS.bg_sound
        sound.set_volume(new_volume)

    for key in SOUNDS:
        if not type(SOUNDS[key]) == type({}): continue
        for sound in SOUNDS[key]:
            our_sound = SOUNDS[key][sound]
            new_volume = our_sound.get_volume() * SETTINGS.master * SETTINGS.sfx
            our_sound.set_volume(new_volume)

def update_setting_sliders():
    MASTER_SLIDER.set_value(SETTINGS.master)
    MASTER_SLIDER_VALUE.set_text(f"{round(MASTER_SLIDER.get_value())}")
    SFX_SLIDER.set_value(SETTINGS.sfx)
    SFX_SLIDER_VALUE.set_text(f"{round(SFX_SLIDER.get_value())}")
    BG_SLIDER.set_value(SETTINGS.bg_sound)
    BG_SLIDER_VALUE.set_text(f"{round(BG_SLIDER.get_value())}")