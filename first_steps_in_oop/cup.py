class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, milliliters):
        space_left = self.size - self.quantity
        if milliliters <= space_left:
            self.quantity += milliliters

    def status(self):
        return self.size - self.quantity