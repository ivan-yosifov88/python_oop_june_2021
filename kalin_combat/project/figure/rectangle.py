from project.figure.figure import Figure


class Rectangle(Figure):
    def calculate_area(self):
        return self.args[0] * self.args[1]

    def calculate_circumference(self):
        return (self.args[0] + self.args[1]) * 2

#
# rectangle = Rectangle("TestRectangle", 2, 4)
# print(rectangle)
