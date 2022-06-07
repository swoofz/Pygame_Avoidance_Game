import pygame
import json
from .game import Game

# Button Click Events
def start_btn(window, display, change_display):
    display.clear_elements()
    display.add_element(Game(window, change_display))
    window.set_display(display)

def quit(settings, scores):
    save_settings(settings)
    save_highscore(scores)
    pygame.quit()
    exit()

def save_settings(settings):
    with open(".\data\saves\settings.json", "w") as f:
        f.write(json.dumps(settings.save(), indent=4))

def save_highscore(scores):
    with open(".\data\saves\highscores.json", "w") as f:
        f.write(json.dumps(scores))

def change_display(window, display):
    window.set_display(display)

def show_highscores(window, display, scores, text):
    display.clear_temp_elements()
    start_x, start_y = (240, 130) 
    offset_x, offset_y = (10, 20)
    for i in range(len(scores)):
        ranking = text.copy()
        ranking.set_text(f"{i+1}.")
        text_w = ranking.text.get_width()
        ranking.position = (start_x - text_w, start_y + (offset_y*i))
        score_text = ranking.copy()
        x, y = score_text.position
        score_text.position = (start_x+offset_x, y)
        score_text.set_text(f"{scores[i]}")

        display.add_temp_element(ranking)
        display.add_temp_element(score_text)
    change_display(window, display)


# Slider events
def change_master_volume(slider, text_ele, settings, sounds):
    settings.set_master(slider.value)
    text_ele.set_text(f"{round(slider.get_value())}")
    update_background_volume(sounds['Background'], settings)
    update_sfx_volume(sounds, settings)

def change_sfx_volume(slider, text_ele, settings, sounds):
    settings.set_sfx(slider.value)
    text_ele.set_text(f"{round(slider.get_value())}")
    update_sfx_volume(sounds, settings)

def change_background_volume(slider, text_ele, settings, sounds):
    settings.set_background_volume(slider.value)
    text_ele.set_text(f"{round(slider.get_value())}")
    update_background_volume(sounds, settings)

def update_background_volume(bg_sounds, settings):
    for sound in bg_sounds:
        sound.set_volume(settings.master * settings.bg_sound)

def update_sfx_volume(all_sounds, settings):
    for key in all_sounds:
        if not type(all_sounds[key]) == type({}): continue
        for sound in all_sounds[key]:
            all_sounds[key][sound].set_volume(settings.master * settings.sfx)


