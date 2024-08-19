import tkinter as tk
from cart import Cart
from product import Product

# database
dd = {'apple': 10, 'banana': 5, 'cherry': 20,'date': 25, 'elderberry': 30, 'fig': 35, 'grape': 40, 'honeydew': 45, 'kiwi': 50, 'lemon': 55, 'mango': 60, 'nectarine': 65, 'orange': 70, 'papaya': 75, 'quince': 80, 'raspberry': 85, 'strawberry': 90, 'tangerine': 95, 'ugli': 100, 'vanilla': 105, 'watermelon': 110, 'ximenia': 115, 'yuzu': 120, 'zucchini': 125}


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shopping Cart")
        self.cart = Cart()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Enter the product you want to add to the cart: quit to exit")
        self.label.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.button = tk.Button(self.root, text="Add to cart", command=self.add_to_cart)
        self.button.pack()

        self.total_label = tk.Label(self.root, text="")
        self.total_label.pack()

    def add_to_cart(self):
        name = self.entry.get()
        if name == 'quit':
            self.show_total()
        elif name in dd:
            price = dd[name]
            product = Product(name, price)
            self.cart.add_product(product)
            self.entry.delete(0, tk.END)
        else:
            self.total_label.config(text="Product not found")

    def show_total(self):
        total = self.cart.calculate_total()
        self.total_label.config(text=f"Total price: {total}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()