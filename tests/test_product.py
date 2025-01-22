from unittest import mock

import pytest
from pytest import CaptureFixture

from src.product import Product


def test_product_init(product_example: Product) -> None:
    """Инициализация объектов класса Product"""
    assert product_example.name == "bottle"
    assert product_example.description == "plastic"
    assert product_example.price == 100.0
    assert product_example.quantity == 2


def test_product_update_setter(capsys: CaptureFixture, product_example: Product) -> None:
    """Проверка на вывод сообщения при отрицательной или нулевой цене"""
    product_example.price = -100.0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"

    product_example.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"

    product_example.price = 1000.0
    assert product_example.price == 1000.0


def test_new_product_is_exist(product_example: Product, product_example2: Product, product_example3: Product) -> None:
    """Тест на обновление существующего продукта"""
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        },
        [product_example, product_example2, product_example3],
    )
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 200000.0
    assert new_product.quantity == 10


def test_new_product_create_from_dict(product_example: Product, product_example3: Product) -> None:
    """Тест на создание объекта из словаря"""
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        },
        [product_example, product_example3],
    )
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5


def test_price_setter_price_decrease_agree(product_example3: Product) -> None:
    """Тест на снижение цены при согласии пользователя и выводы соответствующих сообщений"""
    with mock.patch("builtins.input", return_value="y"):
        product_example3.price = 80.0
    assert product_example3.price == 80.0
    with mock.patch("builtins.print") as mock_print:
        product_example3.price = 80.0
        mock_print.assert_called_once_with("Цена обновлена на 80.0.")


def test_price_setter_price_decrease_disagree(product_example3: Product) -> None:
    """Тест на отказ изменения цены и вывод соответствующих сообщений"""
    with mock.patch("builtins.input", return_value="n"):
        with mock.patch("builtins.print") as mock_print:
            product_example3.price = 80.0
            assert product_example3.price == 210000.0
            mock_print.assert_called_once_with("Цена не была изменена.")


def test_product_str(product_example2: Product) -> None:
    """Тест на строковое представление объекта класса Product"""
    assert str(product_example2) == "Samsung Galaxy S23 Ultra, 200000.0 руб. Остаток: 5 шт."


def test_product_add(product_example3: Product, product_example2: Product) -> None:
    """Тест для проверки сложения экземпляров класса для нахождения полной стоимости всех товаров на складе"""
    assert product_example2 + product_example3 == 2680000.0


def test_product_add_error(product_example2: Product) -> None:
    """Тест на ошибку добавления продукта"""
    with pytest.raises(TypeError):
        _ = product_example2 + 1
