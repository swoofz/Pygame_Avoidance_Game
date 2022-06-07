import pygame
import json
from .sound import Sound, MusicPlayer

pygame.init()
pygame.display.set_caption('Avoidance')
WIDTH = 500
HEIGHT = 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

# COLOR PALETTE
COLOR_1 = (25, 25, 59)      # dark blue
COLOR_2 = (39, 34, 76)      # dark purple-blue
COLOR_3 = (78, 60, 125)     # light purple
COLOR_4 = (109, 50, 105)    # draker magenta
COLOR_5 = (134, 45, 93)     # magenta

with open(".\data\saves\highscores.json", "r") as f:
    HIGH_SCORES = json.load(f)

SOUNDS = {
    "Player": {
        "jump": Sound(".\data\sounds\jump_by-Greencouch.wav", volume=0.6)
    },
    "sounds": {
        "collision": Sound(".\data\sounds\collision_by-likeclockwork.wav")
    },
    "Background":[
        Sound(".\data\sounds\music/bg-1_by-BloodPixelHero.wav"),
        Sound(".\data\sounds\music/bg-2_by-BloodPixelHero.wav"),
        Sound(".\data\sounds\music/bg3-by_PureDesignGirl.mp3", volume=0.7),
        Sound(".\data\sounds\music/bg-4_by-BloodPixelHero.wav", volume=0.85),
        Sound(".\data\sounds\music/bg-5_by-BloodPixelHero.wav", volume=0.8)
    ]
}

MUSIC_PLAYER = MusicPlayer(songs=SOUNDS['Background'])

SETTING_SLIDER_X=200
SETTING_SLIDER_VALUE_X=430
SETTING_SLIDER_TEXT_X=40

START_SETTING_TEXT_Y=223
START_SETTING_SLIDER_Y=230
SPACING=25