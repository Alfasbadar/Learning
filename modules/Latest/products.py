import json
from datetime import datetime

class Product:
    def __init__(self, product_id, name, description, sp, bp, quantity, expiry_date):
        self.id = product_id
        self.name = name
        self.description = description
        self.sp = sp
        self.bp = bp
        self.quantity = quantity
        self.expiry_date = expiry_date

    def __str__(self):
        return f"{self.name} (ID: {self.id}) - Quantity: {self.quantity}, Expiry Date: {self.expiry_date}"

class ProductManager:
    def __init__(self):
        self.product_list = {}

    def add_item(self, product):
        if product.id not in self.product_list:
            self.product_list[product.id] = product
        else:
            print("Product ID already exists. Use update_item to modify an existing item.")

    def remove_item(self, product_id):
        if product_id in self.product_list:
            del self.product_list[product_id]
        else:
            print(f"Product with ID {product_id} not found.")

    def get_product_list(self):
        return list(self.product_list.values())

    def set_product_list(self, product_list):
        self.product_list = {product.id: product for product in product_list}

    def save_to_database(self, filename="product_database.json"):
        data = [{"id": product.id,
                 "name": product.name,
                 "description": product.description,
                 "sp": product.sp,
                 "bp": product.bp,
                 "quantity": product.quantity,
                 "expiry_date": product.expiry_date.strftime("%Y-%m-%d")} for product in self.product_list.values()]

        with open(filename, "w") as file:
            json.dump(data, file, indent=2)

    def load_from_database(self, filename="product_database.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)

            product_list = []
            for item in data:
                expiry_date = datetime.strptime(item["expiry_date"], "%Y-%m-%d")
                product = Product(item["id"], item["name"], item["description"], item["sp"], item["bp"],
                                  item["quantity"], expiry_date)
                product_list.append(product)

            self.set_product_list(product_list)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("Database file not found. Creating a new database.")

# Example usage:
# if __name__ == "__main__":
#     product_manager = ProductManager()

#     # Adding products
#     product_manager.add_item(Product(1, "Product A", "Description A", 10.99, 5.99, 50, datetime(2023, 1, 1)))
#     product_manager.add_item(Product(2, "Product B", "Description B", 19.99, 10.99, 30, datetime(2023, 6, 1)))

#     # Saving to and loading from the database
#     product_manager.save_to_database()
#     product_manager.load_from_database()

#     # Getting the product list
#     products = product_manager.get_product_list()
#     for product in products:
#         print(product)
