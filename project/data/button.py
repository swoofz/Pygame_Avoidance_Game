from pygame import draw, mouse, font

# Base Class
class Button():
    def __init__(self, surface, text, color, size, position, click_event, click_args, font_size, font_family, hover_color, text_color):
        self.surface = surface
        self.text_color = text_color
        self.font = font.SysFont(font_family, font_size)
        self.text = self.font.render(text, True, text_color)
        self.bg = color
        self.hover_color = hover_color
        self.color = self.bg
        self.size = size
        self.position = position
        self.click = click_event
        self.click_args = click_args
        self.button = None
        self.can_press = True

    def click_event(self):
        if self.click == None: return
        self.click(*self.click_args)

    def clicked(self):
        if mouse.get_pressed()[0] and self.can_press:
            self.can_press = False
            return mouse.get_pos()
        if not mouse.get_pressed()[0] and not self.can_press:
            self.can_press = True
        return None

    def hover(self):
        self.color = self.bg
        if self.button.collidepoint(mouse.get_pos()):
            self.color = self.hover_color

    def update(self):
        if not self.button: return
        self.hover()
        pos = self.clicked()
        if pos and self.button.collidepoint(pos):
            self.click_event()



class RectButton(Button):
    def __init__(
        self, surface, text="Defuat Text", bg=(255,255,255), size=(20,20), position=(20,20), click_event=None, click_args=[], font_size=16, font_family="Arial", hover_color=(255,255,255), text_color=(0,0,0)
    ):
        super().__init__(
            surface, text, bg, size, position, click_event, click_args=click_args, font_size=font_size, font_family=font_family, hover_color=hover_color, text_color=text_color
        )
        self.width, self.height = size
        self.rect = (surface, bg, (position, size))

    def center_text(self):
        x, y =  self.position
        textOffx = self.width/2 - self.text.get_width()/2
        textOffy = self.height/2 - self.text.get_height()/2
        self.surface.blit(self.text, (x + textOffx, y + textOffy))

    def draw_border(self):
        x, y = self.position
        draw.rect(
            self.surface, 
            self.text_color, 
            ((x-1,y-1), 
            (self.width+2, self.height+2))
        )

    def draw(self):
        self.update()
        self.rect = (self.surface, self.color, (self.position, self.size))
        self.draw_border()
        self.button = draw.rect(*self.rect)
        self.center_text()