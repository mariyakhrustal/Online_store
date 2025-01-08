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


def test_product_create_from_dict() -> None:
    """Тест на создание объекта из словаря"""
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5
