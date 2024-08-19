import tkinter as tk
from cart import Cart
from product import Product

# database
dd = {'apple': 10, 'banana': 5, 'cherry': 20,'date': 25, 'elderberry': 30, 'fig': 35, 'grape': 40, 'honeydew': 45, 'kiwi': 50, 'lemon': 55, 'mango': 60, 'nectarine': 65, 'orange': 70, 'papaya': 75, 'quince': 80, 'raspberry': 85, 'strawberry': 90, 'tangerine': 95, 'ugli': 100, 'vanilla': 105, 'watermelon': 110, 'ximenia': 115, 'yuzu': 120, 'zucchini': 125}


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Market App")
        self.root.geometry("500x500")
        self.cart = Cart()
        self.create_widgets()