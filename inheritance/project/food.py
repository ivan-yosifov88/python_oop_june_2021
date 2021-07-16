from project.product import Product


class Food(Product):
    PRODUCT_QUANTITY = 15

    def __init__(self, name):
        super().__init__(name, quantity=self.PRODUCT_QUANTITY)
        # self.quantity = self.PRODUCT_QUANTITY
