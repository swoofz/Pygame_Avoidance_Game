from .const import *
from .event_handler import *
from .button import RectButton
from .slider import Slider
from .text import Text, Paragraph
from .display import Display
from .window import Window
from .settings import Settings


# Displays ---------------------------------------------------------------------
# Main Menu
MAIN_MENU = Display(
    WINDOW, 
    elements=[],
    bg_color=COLOR_2
)

# Game
GAME_DISPLAY = Display(
    WINDOW,
    elements=[], 
    bg_color=COLOR_1
)

# Settings
SETTING_DISPLAY = Display(
    WINDOW,
    elements=[], 
    bg_color=COLOR_2
)

# How To Play Screen
INTRUCTION_DISPLAY = Display(
    WINDOW,
    elements=[], 
    bg_color=COLOR_2
)

# Highscores
HIGH_SCORES_DISPLAY = Display(
    WINDOW,
    elements=[], 
    bg_color=COLOR_2
)
# -------------------------------------------------------------------------------


CONTENT = Window(MAIN_MENU)
SETTINGS = Settings()
DEFAULT_TEXT= Text(WINDOW, font_size=20, text_color=COLOR_5)


# Elements ----------------------------------------------------------------------
GAME_TITLE = Text(
    WINDOW,
    position=(160, 130),
    font_size=46,
    text="Avoidance",
    text_color=COLOR_4
)

START_BTN = RectButton(
    WINDOW, 
    size=(100,50), 
    position=(140,400),
    text="Start",
    font_size=20,
    bg=COLOR_1,
    hover_color=COLOR_3,
    text_color=COLOR_5,
    click_event=start_btn,
    click_args=[CONTENT, GAME_DISPLAY, MAIN_MENU]
)

SETTING_BTN = RectButton(
    WINDOW, 
    size=(100,50), 
    position=(250,400),
    text="Setting",
    font_size=20,
    bg=COLOR_1,
    hover_color=COLOR_3,
    text_color=COLOR_5,
    click_event=change_display,
    click_args=[CONTENT, SETTING_DISPLAY]
)

INTRUCTION_BTN = RectButton(
    WINDOW, 
    size=(100,50), 
    position=(140,460),
    text="How To Play",
    font_size=18,
    bg=COLOR_1,
    hover_color=COLOR_3,
    text_color=COLOR_5,
    click_event=change_display,
    click_args=[CONTENT, INTRUCTION_DISPLAY]
)

QUIT_BTN = RectButton(
    WINDOW, 
    size=(100,50), 
    position=(250,460),
    text="Quit",
    bg=COLOR_1,
    hover_color=COLOR_3,
    text_color=COLOR_5,
    font_size=20,
    click_event=quit,
    click_args=[SETTINGS, HIGH_SCORES]
)

HIGH_SCORES_BTN = RectButton(
    WINDOW,
    size=(100,50), 
    position=(200,520),
    text="Highscores",
    font_size=20,
    bg=COLOR_1,
    hover_color=COLOR_3,
    text_color=COLOR_5,
    click_event=show_highscores,
    click_args=[CONTENT, HIGH_SCORES_DISPLAY, HIGH_SCORES, DEFAULT_TEXT]
)

BACK_BTN = RectButton(
    WINDOW, 
    size=(100,50), 
    position=(390,540),
    text="Back",
    font_size=20,
    bg=COLOR_1,
    hover_color=COLOR_3,
    text_color=COLOR_5,
    click_event=change_display,
    click_args=[CONTENT, MAIN_MENU]
)

SETTING_TITLE = Text(
    WINDOW, 
    position=(180, 150),
    text="Settings",
    font_size=42,
    text_color=COLOR_4
)

# SLIDERS ----------------------------------------------------------------------
# Master Volume Slider 
MASTER_SLIDER_TEXT = Text(
    WINDOW,
    position=(SETTING_SLIDER_TEXT_X, START_SETTING_TEXT_Y),
    text="Master Volume",
    font_size=18,
    text_color=COLOR_4
)

MASTER_SLIDER_VALUE = Text(
    WINDOW,
    position=(SETTING_SLIDER_VALUE_X, START_SETTING_TEXT_Y),
    font_size=18,
    text_color=COLOR_4
)

MASTER_SLIDER = Slider(
    position=(SETTING_SLIDER_X, START_SETTING_SLIDER_Y),
    background_color=COLOR_3,
    point_color=COLOR_1,
    slider_color=COLOR_4,
    onchange_event=change_master_volume,
    on_change_args=[MASTER_SLIDER_VALUE, SETTINGS, SOUNDS]
)
MASTER_SLIDER_VALUE.set_text(f"{round(MASTER_SLIDER.get_value())}")

# SFX Volume Slider
SFX_SLIDER_TEXT = Text(
    WINDOW,
    position=(SETTING_SLIDER_TEXT_X, START_SETTING_TEXT_Y+SPACING),
    text="SFX Volume",
    font_size=18,
    text_color=COLOR_4
)

SFX_SLIDER_VALUE = Text(
    WINDOW,
    position=(SETTING_SLIDER_VALUE_X, START_SETTING_TEXT_Y+SPACING),
    font_size=18,
    text_color=COLOR_4
)

SFX_SLIDER = Slider(
    position=(SETTING_SLIDER_X,START_SETTING_SLIDER_Y+SPACING),
    background_color=COLOR_3,
    point_color=COLOR_1,
    slider_color=COLOR_4,
    onchange_event=change_sfx_volume,
    on_change_args=[SFX_SLIDER_VALUE, SETTINGS, SOUNDS]
)
SFX_SLIDER_VALUE.set_text(f"{round(SFX_SLIDER.get_value())}")

# Background Volume Slider
BG_SLIDER_TEXT = Text(
    WINDOW,
    position=(SETTING_SLIDER_TEXT_X, START_SETTING_TEXT_Y+(SPACING*2)),
    text="Background Volume",
    font_size=18,
    text_color=COLOR_4
)

BG_SLIDER_VALUE = Text(
    WINDOW,
    position=(SETTING_SLIDER_VALUE_X, START_SETTING_TEXT_Y+(SPACING*2)),
    font_size=18,
    text_color=COLOR_4
)

BG_SLIDER = Slider(
    position=(SETTING_SLIDER_X,START_SETTING_SLIDER_Y+(SPACING*2)),
    background_color=COLOR_3,
    point_color=COLOR_1,
    slider_color=COLOR_4,
    onchange_event=change_background_volume,
    on_change_args=[BG_SLIDER_VALUE, SETTINGS, SOUNDS['Background']]
)
BG_SLIDER_VALUE.set_text(f"{round(BG_SLIDER.get_value())}")
# ---------------------------- SLIDER END -----------------------------------------


INTRUCTION_TITLE = Text(
    WINDOW,
    position=(170, 100),
    font_size=32,
    text="How To Play",
    text_color=COLOR_4
)

INTRUCTION_PARAGRAPH = Paragraph(
    WINDOW,
    position=(WIDTH*(.25/2), 160),
    font_size=16,
    max_width=WIDTH*.75,
    text=(
        "There are black squares coming from outside the screen to collide with the player. If the player gets hit the game is over. The goal is to get a high score. Score gets increase as long as you survive."
    ),
    text_color=COLOR_4
)

INTRUCTION_KEYS = Text(
    WINDOW,
    position=(200, 300),
    font_size=20,
    text="Key Binds",
    text_color=COLOR_4
)

KEYS_TEXT = Text(
    WINDOW,
    position=(180, 330),
    font_size=16,
    text="Move Up: Left-Click",
    text_color=COLOR_4
)

HIGH_SCORE_TITLE = Text(
    WINDOW,
    position=(150, 60),
    font_size=48,
    text="Highscores",
    text_color=COLOR_4
)
# ----------------------------------------------------------------------------------


# Settings ------------------------------------------------------------------------
SETTINGS.set_master(MASTER_SLIDER.value)
SETTINGS.set_sfx(SFX_SLIDER.value)
SETTINGS.set_background_volume(BG_SLIDER.value)
# ---------------------------------------------------------------------------------


# Adding Display Elements ----------------------------------------------------------
# Main Menu Elements
MAIN_MENU.add_element(GAME_TITLE)
MAIN_MENU.add_element(START_BTN)
MAIN_MENU.add_element(SETTING_BTN)
MAIN_MENU.add_element(INTRUCTION_BTN)
MAIN_MENU.add_element(QUIT_BTN)
MAIN_MENU.add_element(HIGH_SCORES_BTN)

# Setting Elements
SETTING_DISPLAY.add_element(BACK_BTN)
SETTING_DISPLAY.add_element(SETTING_TITLE)

SETTING_DISPLAY.add_element(MASTER_SLIDER)
SETTING_DISPLAY.add_element(MASTER_SLIDER_TEXT)
SETTING_DISPLAY.add_element(MASTER_SLIDER_VALUE)

SETTING_DISPLAY.add_element(SFX_SLIDER)
SETTING_DISPLAY.add_element(SFX_SLIDER_TEXT)
SETTING_DISPLAY.add_element(SFX_SLIDER_VALUE)

SETTING_DISPLAY.add_element(BG_SLIDER)
SETTING_DISPLAY.add_element(BG_SLIDER_TEXT)
SETTING_DISPLAY.add_element(BG_SLIDER_VALUE)

# Intruction elements
INTRUCTION_DISPLAY.add_element(BACK_BTN)
INTRUCTION_DISPLAY.add_element(INTRUCTION_TITLE)
INTRUCTION_DISPLAY.add_element(INTRUCTION_PARAGRAPH)
INTRUCTION_DISPLAY.add_element(INTRUCTION_KEYS)
INTRUCTION_DISPLAY.add_element(KEYS_TEXT)

# Highscores elements
HIGH_SCORES_DISPLAY.add_element(HIGH_SCORE_TITLE)
HIGH_SCORES_DISPLAY.add_element(BACK_BTN)
# --------------------------------------------------------------------------------