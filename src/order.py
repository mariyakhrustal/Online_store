from src.base_item import BaseItem
from src.exceptions import ZeroQuantityError
from src.product import Product


class Order(BaseItem):
    def __init__(self, product: Product, quantity: int):
        if quantity > product.quantity:
            raise ValueError(f"Ошибка: На складе только {product.quantity} шт. товара '{product.name}'.")
        try:
            if product.quantity == 0:
                raise ZeroQuantityError(
                    f"Товар '{product.name}' не может быть добавлен в заказ, так как количество равно 0."
                )
        except ZeroQuantityError as e:
            print(str(e))
        else:
            product.quantity -= quantity
            print(f"Товар '{product.name}' успешно добавлен в заказ.")
        finally:
            print("Обработка добавления товара в заказ завершена.")
        self.product = product
        self.quantity = quantity
        self.total_price = self.product.price * self.quantity

    def __str__(self) -> str:
        return f"Заказ на {self.quantity} шт. '{self.product.name}' по цене \
{self.product.price} руб. Общая стоимость: {self.total_price} руб."
