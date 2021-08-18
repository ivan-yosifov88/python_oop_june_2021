import math

from project.figure.figure import Figure


class Circle(Figure):
    def calculate_area(self):
        return self.args[0] ** 2 * math.pi

    def calculate_circumference(self):
        return 2 * math.pi * self.args[0]



# circle = Circle("CircleTest", 10)
# print(circle.calculate_circumference())
#
# print(circle.calculate_area())
#
# print(circle.relativity())
#
# area = circle.calculate_area()
#
# circumference = circle.calculate_circumference()
#
# result = area / circumference
#
# print(result)
#
# print(circle)