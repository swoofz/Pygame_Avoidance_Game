from pygame import draw, mouse
from .const import WINDOW


class Slider:
    def __init__(
        self, size=(200,8), position=(0,0), background_color=(255,255,255), slider_color=(0,255,0), point_color=(0,0,0), range=(0,100), onchange_event=None, on_change_args=[]
    ):
        self.w, self.h = size
        self.position = position
        self.background_color = background_color
        self.slider_color = slider_color
        self.point_color = point_color
        self.range = range
        self.onchange_event = onchange_event
        self.on_change_args = on_change_args

        self.value_pos = self.w - (self.w/2)
        self.value = self.value_pos/self.w
        self.point = None
        self.dragging = False

    def set_value_pos(self, value_pos):
        if value_pos < 0 or value_pos > self.w: return
        self.value_pos = value_pos
        self.value = self.value_pos/self.w

    def set_value(self, value):
        self.value = value
        self.value_pos = self.w * value

    def get_value(self):
        return (1-self.value)*self.range[0] + self.value*self.range[1]

    def can_drag(self):
        if self.point is None: return
        if mouse.get_pressed()[0]:
            position = mouse.get_pos()
            if self.point.collidepoint(position) and not self.dragging:
                self.offset_x = position[0] - (self.position[0]+self.value_pos)
                self.dragging = True
            return self.dragging
        self.dragging = False
        return False

    def drag(self):
        if not self.can_drag(): return
        x, _ = self.position
        mouse_position = mouse.get_pos()
        value_position = mouse_position[0] + self.offset_x - x
        if value_position < 0: value_position = 0
        if value_position > self.w: value_position = self.w
        self.set_value_pos(value_position)
        if not self.onchange_event: return
        self.onchange_event(self, *self.on_change_args)

    def update(self):
        self.drag()

    def draw(self):
        self.update()
        x, y = self.position
        draw.rect(WINDOW, self.background_color, (self.position, (self.w, self.h)))
        draw.circle(WINDOW, self.background_color, (x+self.w,y+(self.h/2)), self.h/2)
        draw.circle(WINDOW, self.slider_color, (x, y+(self.h/2)), self.h/2)
        draw.rect(WINDOW, self.slider_color, (self.position, (self.value_pos, self.h)))
        self.point = draw.circle(WINDOW, self.point_color, (x+self.value_pos, y+(self.h/2)), self.h)
        draw.circle(WINDOW, self.slider_color, (x+self.value_pos, y+(self.h/2)), self.h/2)