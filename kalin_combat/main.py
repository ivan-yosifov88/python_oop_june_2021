from project.figure.circle import Circle
from project.figure.rectangle import Rectangle
from project.figure.square import Square
from project.figure.triangle import Triangle
from project.game import Game

tri1 = Triangle("tri1", 9, 4, 6.5, 4.5)
tri2 = Triangle("tri2", 5, 2.4, 3, 4)
cir1 = Circle("cir1", 3)
rec1 = Rectangle("rec1", 1, 7)
squ1 = Square("squ1", 6)
g = Game()
print(g.figures.add(tri1))
print(g.figures.add(tri2))
print(g.figures.add(cir1))
print(g.figures.add(rec1))
print(g.figures.add(squ1))
print(g.area_battle(cir1, tri1))
print(g.circumference_battle(cir1, tri1))
print(g.relative_battle(cir1, tri1))
print(g.figures.remove("squ1"))
print(g.figures)
print("-------------")
print(g)
