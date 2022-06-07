from pygame import mouse, draw

class Player:
    def __init__(self, color, size, position, sounds={}):
        self.color = color
        self.size = size
        self.x, self.y = position
        self.position = position
        self.can_move = True
        self.speed = 5
        self.sounds = sounds

    def fly_up(self):
        if mouse.get_pressed()[0] and self.can_move: 
            self.sounds['jump'].play()
            self.speed = -6
            self.can_move = False
        if not mouse.get_pressed()[0] and not self.can_move:
            self.can_move = True

    def draw(self, win):
        self.us = draw.circle(win, self.color, self.position, self.size)

    def update(self):
        self.speed += 0.23
        if self.speed > 5: self.speed = 5

        self.y += self.speed
        self.fly_up()
        self.position = (self.x, self.y)
