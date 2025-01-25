from pytest import CaptureFixture

from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_product_mixin(capsys: CaptureFixture) -> None:
    """Тест на вывод информации при создании экземпляров классов"""
    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 200000.0, 5)
    message = capsys.readouterr()
    assert message.out.strip() == "Product('Samsung Galaxy S23 Ultra', '256GB, Серый цвет, 200MP камера', 200000.0, 5)"

    Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone('Xiaomi Redmi Note 11', '1024GB, Синий', 31000.0, 14)"

    LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass('Газонная трава 2', 'Выносливая трава', 450.0, 15)"
