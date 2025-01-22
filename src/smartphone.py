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
