class Display:
    def __init__(self, surface, bg_color=(255, 255, 255), elements=[]):
        if not type(elements) == type([]): 
            raise Exception(f"Display can't be initialized, elements needs to be a list. You pass {elements}")

        self.surface = surface
        self.background_color = bg_color
        self.elements = elements

    def add_element(self, element):
        self.elements.append(element)
        self.ele_len = len(self.elements)
    
    def clear_elements(self):
        self.elements = []

    def add_temp_element(self, element):
       self.elements.append(element)

    def clear_temp_elements(self):
        self.elements = self.elements[:self.ele_len]

    def draw(self):
        self.surface.fill(self.background_color)
        for ele in self.elements:
            ele.draw()