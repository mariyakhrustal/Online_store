import pytest

from src.category import Category
from src.product import Product
from src.product_iterator import ProductIterator


def test_category_init(category_example1: Category, category_example2: Category) -> None:
    """Инициализация объектов класса Category"""
    assert category_example1.name == "packaging"
    assert category_example1.description == "packaging for drinks"
    assert category_example1.products_in_list == []

    assert category_example2.name == "packaging"
    assert category_example2.description == "packaging for milk"
    assert len(category_example2.products_in_list) == 3

    assert category_example1.category_count == 2
    assert category_example2.category_count == 2

    assert category_example1.product_count == 3
    assert category_example2.product_count == 3


def test_category_products_property(category_example1: Category, category_example2: Category) -> None:
    """Тест на создание строк для просмотра товаров"""
    assert category_example1.products == ""
    assert category_example2.products == (
        "bottle, 200.0 руб. Остаток: 1 шт.\n"
        "Tetra Pak, 300.0 руб. Остаток: 4 шт.\n"
        "bottle, 100.0 руб. Остаток: 3 шт.\n"
    )


def test_category_add_product(category_example2: Category, product_example: Product) -> None:
    """Тест на добавление нового продукта"""
    assert len(category_example2.products_in_list) == 3
    category_example2.add_product(product_example)
    assert len(category_example2.products_in_list) == 4


def test_category_str(category_example3: Category) -> None:
    """Тест на строковое представление объекта класса Category"""
    assert str(category_example3) == "Смартфоны, количество продуктов: 27 шт."


def test_product_iterator(product_iterator: ProductIterator) -> None:
    """Тест на перебор товаров одной категории"""
    iter(product_iterator)
    assert product_iterator.index == 0

    assert next(product_iterator).name == "Samsung Galaxy S23 Ultra"
    assert next(product_iterator).name == "Iphone 15"
    assert next(product_iterator).name == "Xiaomi Redmi Note 11"

    with pytest.raises(StopIteration):
        next(product_iterator)
