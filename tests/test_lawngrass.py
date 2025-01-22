import pytest

from src.lawngrass import LawnGrass


def test_grass_init(product_grass1: LawnGrass) -> None:
    """Инициализация объектов класса LawnGrass"""
    assert product_grass1.name == "Газонная трава"
    assert product_grass1.description == "Элитная трава для газона"
    assert product_grass1.price == 500.0
    assert product_grass1.quantity == 20
    assert product_grass1.country == "Россия"
    assert product_grass1.germination_period == "7 дней"
    assert product_grass1.color == "Зеленый"


def test_grass_add(product_grass1: LawnGrass, product_grass2: LawnGrass) -> None:
    """Тест на добавление продукта LawnGrass"""
    assert product_grass1 + product_grass2 == 16750.0


def test_grass_add_error(product_grass2: LawnGrass) -> None:
    """Тест на ошибку добавления продукта LawnGrass"""
    with pytest.raises(TypeError):
        _ = product_grass2 + 1
