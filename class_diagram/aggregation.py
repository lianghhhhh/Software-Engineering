class Customer:
    def __init__(self, name: str):
        self.name = name
        self.orders = []

    def add_order(self, order: 'Order'):
        self.orders.append(order)
        order.customer = self

class Order:
    def __init__(self, product: str, quantity: int):
        self.product = product
        self.quantity = quantity
        self.customer = None

    def print_order(self):
        print(f"{self.customer.name} ordered {self.quantity} {self.product}")

if __name__ == "__main__":
    alice = Customer("Alice")
    tom = Customer("Tom")
    
    alice.add_order(Order("Apples", 5))
    alice.add_order(Order("Bananas", 10))
    tom.add_order(Order("Cherries", 15))
    tom.add_order(Order("Oranges", 20))

    print("Customer Orders:")
    for customer in [alice, tom]:
        for order in customer.orders:
            order.print_order()