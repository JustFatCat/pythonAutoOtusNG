from src.Rectangle import Rectangle

class Square(Rectangle):
    """This is Square class"""

    def __init__(self, side):
        super().__init__(side, side)
        if side <= 0:
            raise ValueError("Can't create Square")
        self.side = side
        self.name = f"Square {side}"