import math as m

class vector:
    def __init__(self, component1 : float, component2 : float) -> None:
        self.X = component1
        self.Y = component2

    def __add__(self, other):
        x = self.X + other.X
        y = self.Y + other.Y
        return vector(x,y)
    
    def __sub__(self, other):
        x = self.X - other.X
        y = self.Y - other.Y
        return vector(x,y)

    def __mul__(self, scalar : float):
        x = self.X * scalar
        y = self.Y * scalar
        return vector(x,y)
    
    def abs(self):
        absoluteValue = m.sqrt(self.X**2 + self.Y**2)
        return absoluteValue

