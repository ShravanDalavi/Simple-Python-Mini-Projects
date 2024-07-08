class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

class Sale:
    def __init__(self, sale_id, customer_id, product_id, quantity, total_price):
        self.sale_id = sale_id
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity
        self.total_price = total_price

class GroceryStore:
    def __init__(self):
        self.products = {}
        self.customers = {}
        self.sales = {}
        self.next_product_id = 1
        self.next_customer_id = 1
        self.next_sale_id = 1

    # Inventory Management
    def add_product(self, name, price, quantity):
        product = Product(self.next_product_id, name, price, quantity)
        self.products[self.next_product_id] = product
        self.next_product_id += 1
        print(f"Product added: {product.name}, ID: {product.product_id}")

    def update_product(self, product_id, name=None, price=None, quantity=None):
        if product_id in self.products:
            product = self.products[product_id]
            if name:
                product.name = name
            if price:
                product.price = price
            if quantity:
                product.quantity = quantity
            print(f"Product updated: {product.name}, ID: {product.product_id}")
        else:
            print(f"Product ID {product_id} not found.")

    def view_products(self):
        print("\nProduct List:")
        for product in self.products.values():
            print(f"ID: {product.product_id}, Name: {product.name}, Price: ${product.price}, Quantity: {product.quantity}")

    # Customer Management
    def add_customer(self, name, email):
        customer = Customer(self.next_customer_id, name, email)
        self.customers[self.next_customer_id] = customer
        self.next_customer_id += 1
        print(f"Customer added: {customer.name}, ID: {customer.customer_id}")

    def view_customers(self):
        print("\nCustomer List:")
        for customer in self.customers.values():
            print(f"ID: {customer.customer_id}, Name: {customer.name}, Email: {customer.email}")

    # Sales Tracking
    def record_sale(self, customer_id, product_id, quantity):
        if customer_id in self.customers and product_id in self.products:
            product = self.products[product_id]
            if product.quantity >= quantity:
                total_price = product.price * quantity
                sale = Sale(self.next_sale_id, customer_id, product_id, quantity, total_price)
                self.sales[self.next_sale_id] = sale
                self.next_sale_id += 1
                product.quantity -= quantity
                print(f"Sale recorded: Sale ID {sale.sale_id}, Total Price: ${total_price}")
            else:
                print("Insufficient product quantity.")
        else:
            print("Invalid customer ID or product ID.")

    def view_sales(self):
        print("\nSales List:")
        for sale in self.sales.values():
            print(f"Sale ID: {sale.sale_id}, Customer ID: {sale.customer_id}, Product ID: {sale.product_id}, Quantity: {sale.quantity}, Total Price: ${sale.total_price}")

def main():
    store = GroceryStore()

    while True:
        print("\nGrocery Store Management System")
        print("1. Add Product")
        print("2. Update Product")
        print("3. View Products")
        print("4. Add Customer")
        print("5. View Customers")
        print("6. Record Sale")
        print("7. View Sales")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            store.add_product(name, price, quantity)
        elif choice == "2":
            product_id = int(input("Enter product ID: "))
            name = input("Enter new product name (leave blank to keep current): ")
            price = input("Enter new product price (leave blank to keep current): ")
            quantity = input("Enter new product quantity (leave blank to keep current): ")
            store.update_product(product_id, name if name else None, float(price) if price else None, int(quantity) if quantity else None)
        elif choice == "3":
            store.view_products()
        elif choice == "4":
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            store.add_customer(name, email)
        elif choice == "5":
            store.view_customers()
        elif choice == "6":
            customer_id = int(input("Enter customer ID: "))
            product_id = int(input("Enter product ID: "))
            quantity = int(input("Enter quantity: "))
            store.record_sale(customer_id, product_id, quantity)
        elif choice == "7":
            store.view_sales()
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
