from product import Product

class Cart:
    def __init__(self):
        self.products = []
<<<<<<< HEAD

    def add_product(self, product):
        self.products.append(product)

=======
    
    def add_product(self, product):
        self.products.append(product)
    
>>>>>>> umair
    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product.price
        return total
    
    def __repr__(self):
        return f"Cart({self.products!r})"
<<<<<<< HEAD
    
=======






>>>>>>> umair
