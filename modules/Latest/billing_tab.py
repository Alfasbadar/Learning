import tkinter as tk
from tkinter import ttk
from products import Product,ProductManager

class BillingTab(tk.Frame):
    

    
    def __init__(self, parent, *args, **kwargs):
        # product_list=ProductManager.get_product_list
        tk.Frame.__init__(self, parent, *args, **kwargs)

        label = ttk.Label(self, text="Billing Tab Content")
        label.pack(padx=10, pady=10)
