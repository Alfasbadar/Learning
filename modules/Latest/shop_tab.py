import tkinter as tk
from tkinter import ttk
from test_database import ArrayListGenerator

class ShopTab(tk.Frame):
    def __init__(self, parent, product_list=None, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.product_list = product_list or ArrayListGenerator.generate_product_tuple()

        # Create a canvas and add a scrollbar
        self.canvas = tk.Canvas(self, borderwidth=0, background="#ffffff")
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="top", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.scrollable_frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)

        self.create_card_views()

def create_card_views(self):
    for product in self.product_list:
        card_view = ttk.Frame(self.scrollable_frame, borderwidth=2, relief="solid", padding=(10, 10))
        card_view.pack(fill="both", padx=10, pady=10, expand=True)

        label_id = ttk.Label(card_view, text=f"{product.id}")
        label_id.grid(row=0, column=0, padx=5)

        label_name = ttk.Label(card_view, text=f"{product.name}")
        label_name.grid(row=0, column=1, padx=5)

        label_quantity = ttk.Label(card_view, text=f"Quantity: {product.quantity} nos")
        label_quantity.grid(row=0, column=2, padx=5)

        label_price = ttk.Label(card_view, text=f"Price: {product.sp} rs")
        label_price.grid(row=0, column=3, padx=5)

        label_expiry = ttk.Label(card_view, text=f"Expire on: {product.expiry_date}")
        label_expiry.grid(row=0, column=4, padx=5)

        # Bind the card view to an event (e.g., <Button-1> for left click)
        card_view.bind("<Button-1>", lambda event, product=product: self.show_product_details(product))

    # Add "The end" text at the bottom
    ttk.Label(self.scrollable_frame, text="The end", font=("Helvetica", 16)).pack(pady=10)

    def show_product_details(self, product):
        # You can implement the logic to expand the card view and show additional details here.
        print(f"Product Details: {product}")
        # For example, you can create a new window or update the existing UI to show expanded details.

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        self.canvas.itemconfig(self.scrollable_frame, width=event.width)
