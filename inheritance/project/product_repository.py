class ProductRepository:
    def __init__(self):
        self.products = []

    def __repr__(self):
        return '\n'.join(f"{product.name}: {product.quantity}" for product in self.products)

    @staticmethod
    def find_object(list_of_obj, obj_name):
        return [obj for obj in list_of_obj if obj.name == obj_name]

    def add(self, product):
        self.products.append(product)

    def find(self, product_name):
        # fod_sfs = self.find_object(self.products, product_name)
        filter_products = self.find_object(self.products, product_name)
        if filter_products:
            found_product_object = filter_products[0]
            return found_product_object

    def remove(self, product_name):
        filter_products = self.find_object(self.products, product_name)
        if filter_products:
            self.products.remove(filter_products[0])



