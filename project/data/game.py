import random
from pygame import time

from data.button import RectButton
from .player import Player
from .bird import Bird
from .text import Text
from data.const import (
    WIDTH, HEIGHT, WINDOW, SOUNDS, HIGH_SCORES, 
    COLOR_2, COLOR_3, COLOR_4, COLOR_5
)


class Game:
    def __init__(self, window, display):
        self.window = window
        self.display = display
        self.running = True
        self.clock = time.Clock()
        self.player = Player(COLOR_4, 25, (WIDTH/2,HEIGHT/2), sounds=SOUNDS["Player"])
        self.spawn_timer = 0
        self.birds = []
        self.counter = 0
        self.score = 0
        self.score_text = Text(WINDOW, position=(400, 20), font_size=16, text_color=COLOR_5)
        self.spawn_count = [1,3]
        self.increase_level = 15
        self.more_spawn = False
        self.gameover_elements()

    def spawn_bird(self):
        self.spawn_timer -= 0.1
        if not self.spawn_timer < 0: return

        spawn_number = random.randint(*self.spawn_count)
        for _ in range(spawn_number):
            pick_side = random.randint(1,2)

            if pick_side == 1: x = random.randint(-100,-40)
            else: x = random.randint(540,600)
            y = random.randint(25,HEIGHT-25)

            self.birds.append(Bird((0,0,0), (25,10), (x,y), pick_side, random.randint(1,4)))
        self.spawn_timer = random.randint(5,10)

    def remove_birds(self):
        for bird in self.birds:
            if bird.x < -150 or bird.x > 650: self.birds.remove(bird)

    def update_birds(self):
        for bird in self.birds:
            bird.update()
            bird.draw(WINDOW)

    def update_score(self):
        self.counter += 1
        if self.counter % 60 == 0:
            self.score += 1
        self.score_text.set_text(f"Score: {self.score}")
        self.score_text.draw()

        if not self.score == 0 and self.score % self.increase_level == 0 and not self.more_spawn:
            self.more_spawn = True
            self.spawn_count[1] += 1
            if self.score % (self.increase_level*2) == 0: self.spawn_count[0] += 1
        if not self.score % self.increase_level == 0 and self.more_spawn: self.more_spawn=False

    def gameover(self):
        if self.player.y < 0 or self.player.y > HEIGHT: return True
        for bird in self.birds:
            if self.player.us.collidepoint(bird.position):
                SOUNDS['sounds']['collision'].play()
                return True
        return False

    def update_scores(self, max_scores):
        HIGH_SCORES.append(self.score)
        HIGH_SCORES.sort(reverse=True)
        while len(HIGH_SCORES) > max_scores: HIGH_SCORES.pop()

    def gameover_elements(self):
        self.gameover_text = Text(
            WINDOW, 
            position=(WIDTH/2 - 120, HEIGHT/2 - 48), 
            font_size=48, 
            text_color=COLOR_5, 
            text="GAMEOVER"
        )

        self.return_btn = RectButton(
            WINDOW, 
            size=(180,50), 
            position=(20,HEIGHT-60),
            text="Return to Main Menu",
            font_size=20,
            bg=COLOR_2,
            hover_color=COLOR_3,
            text_color=COLOR_5,
            click_event=self.window.set_display,
            click_args=[self.display]
        )

    def draw(self):
        if not self.running:
            self.gameover_text.draw()
            self.return_btn.draw()
            return
        self.clock.tick(60)

        self.spawn_bird()
        self.remove_birds()
        self.update_birds()
        
        self.player.update()
        self.player.draw(WINDOW)
        self.update_score()

        if self.gameover():
            self.update_scores(15)
            last_score = Text(
                WINDOW, 
                position=(195, 175), 
                font_size=16,
                text_color=COLOR_4,
                text=f"You last scored: {self.score}"
            )

            self.running = False
            self.display.clear_temp_elements()
            self.display.add_temp_element(last_score)