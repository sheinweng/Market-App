from product import Product
from cart import Cart

dd = {'apple': 10, 'banana': 5, 'cherry': 20,'date': 25, 'elderberry': 30, 'fig': 35, 'grape': 40, 'honeydew': 45, 'kiwi': 50, 'lemon': 55, 'mango': 60, 'nectarine': 65, 'orange': 70, 'papaya': 75, 'quince': 80, 'raspberry': 85, 'strawberry': 90, 'tangerine': 95, 'ugli': 100, 'vanilla': 105, 'watermelon': 110, 'ximenia': 115, 'yuzu': 120, 'zucchini': 125}

n = input("Enter the number of products you want to add to the cart: ")
n = int(n)
cart = Cart()
for i in range(n):
    name = input("Enter the product you want to add to the cart: ")
    if name in dd:
        price = dd[name]
        product = Product(name, price)
        cart.add_product(product)
    else:
        print("Product not found")
print(cart.calculate_total())
