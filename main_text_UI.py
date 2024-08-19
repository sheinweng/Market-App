from product import Product
from cart import Cart


dd = {'apple': 10, 'banana': 5, 'cherry': 20,'date': 25, 'elderberry': 30, 'fig': 35, 'grape': 40, 'honeydew': 45, 'kiwi': 50, 'lemon': 55, 'mango': 60, 'nectarine': 65, 'orange': 70, 'papaya': 75, 'quince': 80, 'raspberry': 85, 'strawberry': 90, 'tangerine': 95, 'ugli': 100, 'vanilla': 105, 'watermelon': 110, 'ximenia': 115, 'yuzu': 120, 'zucchini': 125}


cart = Cart() #instance of Cart class
while True:
    name = input("Enter the product you want to add to the cart: quit to exit: ")
    if name =='quit':
        break
    if name in dd:
        price = dd[name] # getting the price of the product from the dictionary
        product = Product(name, price)
        cart.add_product(product)
    else:
        print("Product not found")
print(cart.calculate_total()) # calculating the total price of the products in the cart