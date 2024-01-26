import tkinter as tk
from tkinter import ttk

from shop_tab import ShopTab
from management_tab import ManagementTab
from billing_tab import BillingTab

from products import Product,ProductManager
from test_database import ArrayListGenerator

class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Tabbed Panes Example")

        print("Loading test data")
        arraylist=ArrayListGenerator.generate_product_tuple()

        # productmanager=ProductManager
        # Arraylisy=productmanager.get_product_list
        # print("loading from database")
        # print("Loaded database")
        # print("saving to database")
        # productmanager.set_product_list(self,arraylist)
        # productmanager.save_to_database
        # print("Saved to database")
    
        



        container = ttk.Notebook(self)
        shop_tab = ShopTab(container)
        container.add(shop_tab, text="Shop")

        management_tab = ManagementTab(container)
        container.add(management_tab, text="Management")

        billing_tab = BillingTab(container)
        container.add(billing_tab, text="Billing")
        container.pack(expand=True, fill="both")



if __name__ == "__main__":
    app = MainApplication()
    app.geometry("800x600")  # Set the initial window size
    app.mainloop()
