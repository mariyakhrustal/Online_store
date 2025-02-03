import pytest
from pytest import CaptureFixture

from src.category import Category
from src.product import Product
from src.product_iterator import ProductIterator
from src.smartphone import Smartphone


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


def test_category_add_product_error(category_example2: Category) -> None:
    """Тест на ошибку добавления нового продукта"""
    with pytest.raises(TypeError):
        category_example2.add_product("Not a product")


def test_category_add_product_smartphone(category_example2: Category, product_smartphone1: Smartphone) -> None:
    """Тест на добавление нового продукта"""
    category_example2.add_product(product_smartphone1)
    assert category_example2.products_in_list[-1].name == "Iphone 15"


def test_middle_price(category_example3: Category, category_example1: Category) -> None:
    """Тест на вычисление средней цены товаров"""
    assert category_example3.middle_price() == 140333.33
    assert category_example1.middle_price() == 0


def test_category_custom_exception(capsys: CaptureFixture, category_example3: Category) -> None:
    """Тест на работу кастомного исключения в категории"""
    assert len(category_example3.products_in_list) == 3

    product_add = Product("Iphone 12", "512GB, Gray space", 210000.0, 1)
    product_add.quantity = 0
    category_example3.add_product(product_add)
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2] == "Товар 'Iphone 12' не может быть добавлен, количество равно 0."
    assert message.out.strip().split("\n")[-1] == "Обработка добавления товара завершена."

    product_add = Product("Iphone 12", "512GB, Gray space", 210000.0, 1)
    category_example3.add_product(product_add)
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2] == "Товар 'Iphone 12' успешно добавлен в категорию."
    assert message.out.strip().split("\n")[-1] == "Обработка добавления товара завершена."
