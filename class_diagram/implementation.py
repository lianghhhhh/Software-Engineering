from abc import ABC, abstractmethod

class IService(ABC):
    @abstractmethod
    def add(self, item: str) -> None:
        pass

    @abstractmethod
    def remove(self, item: str) -> None:
        pass

class CarService(IService):
    def __init__(self):
        self.cars = []

    def add(self, item: str) -> None:
        self.cars.append(item)

    def remove(self, item: str) -> None:
        self.cars.remove(item)

class BookService(IService):
    def __init__(self):
        self.books = []

    def add(self, item: str) -> None:
        self.books.append(item)

    def remove(self, item: str) -> None:
        self.books.remove(item)

if __name__ == "__main__":
    car_service = CarService()
    book_service = BookService()

    car_service.add("Toyota")
    car_service.add("Honda")
    book_service.add("1984")
    book_service.add("Brave New World")

    print("Cars:", car_service.cars)
    print("Books:", book_service.books)