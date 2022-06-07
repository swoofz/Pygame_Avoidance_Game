from pygame import draw


class Bird:
    def __init__(self, color, size, position, direction, speed):
        self.color = color
        self.size = size
        self.x, self.y = position
        self.position = position
        self.speed = speed # between 5 and 9
        if direction == 1: self.direction = 1
        else: self.direction = -1

    def draw(self, win):
        self.us = draw.rect(win, self.color, (self.position, self.size))

    def update(self):
        self.x += self.speed * self.direction
        self.position = (self.x, self.y)