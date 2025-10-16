class FruitSupplier:
    def __init__(self):
        self.apples = 100
        self.bananas = 50
    
class Client:
    def __init__(self, supplier: FruitSupplier):
        self.supplier = supplier

    def buy_apples(self, quantity: int):
        if quantity <= self.supplier.apples:
            self.supplier.apples -= quantity
            print(f"Bought {quantity} apples")
        else:
            print("Not enough apples available")

    def buy_bananas(self, quantity: int):
        if quantity <= self.supplier.bananas:
            self.supplier.bananas -= quantity
            print(f"Bought {quantity} bananas")
        else:
            print("Not enough bananas available")

if __name__ == "__main__":
    supplier = FruitSupplier()
    clientA = Client(supplier)
    clientB = Client(supplier)

    clientA.buy_apples(30)
    clientB.buy_bananas(20)
    clientA.buy_bananas(80)  # Should indicate not enough bananas available