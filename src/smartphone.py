from src.product import Product


class Smartphone(Product):
    def __init__(self, name,  description,  price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other: "Smartphone") -> float:
        if type(other) is Smartphone:
            total_amount = self.price * self.quantity + other.price * other.quantity
            return total_amount
        raise TypeError


if __name__ == '__main__':
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")
    product1 = Product("Apple", "green apple", 150.0, 2)
    print(smartphone3 + smartphone2)
