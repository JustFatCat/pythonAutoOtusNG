from src.Figure import Figure

class Circle(Figure):
    """This is Circle class"""
    P_CONSTANT = 3.14

    def __init__(self, radius):
        super().__init__()
        if radius <= 0:
            raise ValueError("Can't create Circle")
        self.radius = radius
        self.name = f"Circle {radius}"

    def get_area(self):
        return self.P_CONSTANT * (self.radius * self.radius)

    def get_perimeter(self):
        return 2 * self.P_CONSTANT * self.radius