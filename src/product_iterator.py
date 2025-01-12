from typing import Any

from src.category import Category
from src.product import Product


class ProductIterator:
    def __init__(self, category_obj: Category):
        self.category: Category = category_obj
        self.index: int = 0

    def __iter__(self) -> "ProductIterator":
        self.index = 0
        return self

    def __next__(self) -> Any:
        if self.index < len(self.category.products_in_list):
            product = self.category.products_in_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration


# Пример использования.
if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    iterator = ProductIterator(category1)

    for product in iterator:
        print(product)
