import pytest

from src.lawngrass import LawnGrass
from src.order import Order
from src.smartphone import Smartphone


def test_order_init(product_grass2: LawnGrass) -> None:
    """Тест на инициализацию заказа"""
    order = Order(product_grass2, 4)
    assert order.product.name == "Газонная трава 2"
    assert order.quantity == 4
    assert order.total_price == 1800.0


def test_order_init_error(product_smartphone2: Smartphone) -> None:
    """Тест на выброс исключения при указании большего количества товара, чем есть на складе"""
    with pytest.raises(ValueError) as exc_info:
        Order(product_smartphone2, 15)
    assert (
        str(exc_info.value)
        == f"Ошибка: На складе только {product_smartphone2.quantity} шт. товара '{product_smartphone2.name}'."
    )


def test_order_str(product_grass2: LawnGrass) -> None:
    """Тест на строковое представление объекта класса Order"""
    order = Order(product_grass2, 3)
    expected_str = "Заказ на 3 шт. 'Газонная трава 2' по цене 450.0 руб. Общая стоимость: 1350.0 руб."
    assert str(order) == expected_str
