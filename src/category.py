from typing import Any

from src.base_item import BaseItem
from src.exceptions import ZeroQuantityError
from src.product import Product


class Category(BaseItem):
    name: str
    description: str
    products: list
    product_count = 0
    category_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product) -> None:
        if isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise ZeroQuantityError(
                        f"Товар '{product.name}' не может быть добавлен, так как количество равно 0."
                    )
            except ZeroQuantityError as e:
                print(str(e))
            else:
                self.__products.append(product)
                Category.product_count += 1
                print(f"Товар '{product.name}' успешно добавлен в категорию.")
            finally:
                print("Обработка добавления товара завершена.")
        else:
            raise TypeError

    @property
    def products(self) -> str:
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str

    @property
    def products_in_list(self) -> list:
        return self.__products

    def middle_price(self) -> Any:
        try:
            avg_result = sum([product.price for product in self.__products]) / len(self.__products)
            return round(avg_result, 2)
        except ZeroDivisionError:
            return 0
