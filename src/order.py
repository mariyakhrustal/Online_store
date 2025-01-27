from src.base_item import BaseItem
from src.product import Product


class Order(BaseItem):
    def __init__(self, product: Product, quantity: int):
        if quantity > product.quantity:
            raise ValueError(f"Ошибка: На складе только {product.quantity} шт. товара '{product.name}'.")
        self.product = product
        self.quantity = quantity
        self.total_price = self.product.price * self.quantity

    def __str__(self) -> str:
        return f"Заказ на {self.quantity} шт. '{self.product.name}' по цене \
{self.product.price} руб. Общая стоимость: {self.total_price} руб."
