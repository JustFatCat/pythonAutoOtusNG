from src.Figure import Figure

class Triangle(Figure):
    """This is Triangle class"""

    def __init__(self, side_a, side_b, side_c):
        super().__init__()
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Can't create Triangle")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.name = f"Triangle {side_a} and {side_b} and {side_c}"

        # calculate the semi-perimeter
        self.s = (side_a + side_b + side_c)/2

    def get_area(self):
        return (self.s * (self.s - self.side_a) * (self.s - self.side_b) * (self.s - self.side_c)) * 0.5

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c
