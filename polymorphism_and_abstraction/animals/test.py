from animals.cat import Cat
from animals.dog import Dog
from animals.kitten import Kitten
from animals.tomcat import Tomcat

cat = Cat("Gosho", 20, "Male")
dog= Dog("Pesho", 15, "Male")
kitten = Kitten("bibi", 34)
tomcat = Tomcat("vani", 33)

animals = [cat, dog, kitten, tomcat]

for animal in animals:
    print(animal)
    print(animal.make_sound())