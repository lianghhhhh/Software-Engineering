class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        print(f"Engine with {self.horsepower} HP started.")

class Car:
    def __init__(self, make: str, model: str, engine: Engine):
        self.make = make
        self.model = model
        self.engine = engine  # Composition: Car has an Engine

    def start_car(self):
        print(f"Starting {self.make} {self.model}.")
        self.engine.start()

if __name__ == "__main__":
    engine = Engine(150)
    car = Car("Toyota", "Corolla", engine)
    car.start_car()