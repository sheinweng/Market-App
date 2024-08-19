

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product({self.name!r}, {self.price!r})"
    
    def getprice(self):
<<<<<<< HEAD
        return self.price
=======
        return self.price
    
>>>>>>> umair
