class Window:
    def __init__(self, display):
        self.display = display

    def set_display(self, display):
        self.display = display

    def display_window(self):
        self.display.draw()