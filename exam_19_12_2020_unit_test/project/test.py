from project.factory.paint_factory import PaintFactory

pf = PaintFactory("Gosho", 10)
pf.add_ingredient("blue", 5)
print(pf.products)
pf.add_ingredient("Gosho", 5)
pf.remove_ingredient("gosho", 5)