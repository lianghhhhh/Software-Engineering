# reference: https://www.geeksforgeeks.org/system-design/factory-method-for-designing-pattern/

from abc import ABC, abstractmethod

# Library classes
class Vehicle(ABC):
    @abstractmethod
    def printVehicle(self):
        pass

class TwoWheeler(Vehicle):
    def printVehicle(self):
        print("I am two wheeler")

class FourWheeler(Vehicle):
    def printVehicle(self):
        print("I am four wheeler")

# Client (or user) class
class Client:
    def __init__(self, type):
        if type == 1:
            self.pVehicle = TwoWheeler()
        elif type == 2:
            self.pVehicle = FourWheeler()
        else:
            self.pVehicle = None

    def cleanup(self):
        if self.pVehicle is not None:
            self.pVehicle = None

    def getVehicle(self):
        return self.pVehicle

# Driver program
def main():
    pClient = Client(1)
    pVehicle = pClient.getVehicle()
    if pVehicle is not None:
        pVehicle.printVehicle()
    pClient.cleanup()

if __name__ == "__main__":
    main()