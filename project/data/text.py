from pygame import font


class Text:
    def __init__(
        self, surface, position=(0,0), font_family="Arial", font_size=12, text="Defualt Text", text_color=(0,0,0)
    ):
        self.surface = surface
        self.text_color = text_color
        self.font = font.SysFont(font_family, font_size, True)
        self.text = self.font.render(text, True, text_color)
        self.position = position
        self.font_size = font_size

    def copy(self):
        return Text(
            surface=self.surface,
            position=self.position,
            font_family="Arial",
            font_size=self.font_size,
            text="Defualt Text",
            text_color=self.text_color
        )

    def set_font_size(self, font_size):
        self.font_size = font_size

    def set_font_family(self, font_family):
        self.font = font.SysFont(font_family, self.font_size)

    def set_text_color(self, color):
        self.text_color = color

    def set_text(self, text):
        self.text = self.font.render(text, True, self.text_color)

    def draw(self):
        self.surface.blit(self.text, self.position)


class Paragraph(Text):
    def __init__(
        self, surface, position=(0,0), font_family="Arial", font_size=12, text="Defualt Text", text_color=(0,0,0), 
        max_width=200
    ): 
        super().__init__(
            surface=surface, position=position, font_family=font_family, font_size=font_size, text=text, text_color=text_color
        )
        self.max_width = max_width
        self.paragraph = text.split()
        self.lines = []
        self.get_lines()

    def get_lines(self):
        string = ""
        for word in self.paragraph:
            string += word + " "
            if self.font.render(string, True, self.text_color).get_width() < self.max_width:
                text = self.font.render(string, True, self.text_color)
            else:
                self.lines.append(text)
                string = "" + word + " "
        self.lines.append(text)

    def draw(self):
        x, y = self.position
        for i in range(len(self.lines)):
            self.surface.blit(self.lines[i], (x,y+(self.lines[i].get_height()*i)))