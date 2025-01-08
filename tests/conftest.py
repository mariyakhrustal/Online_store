import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product_example() -> Product:
    return Product("bottle", "plastic", 100.0, 2)


@pytest.fixture
def category_example1() -> Category:
    return Category("packaging", "packaging for drinks", [])


@pytest.fixture
def category_example2() -> Category:
    return Category(
        "packaging",
        "packaging for milk",
        products=[
            Product("bottle", "glass", 200.0, 1),
            Product("Tetra Pak", "cardboard", 300.0, 4),
            Product("bottle", "plastic", 100.0, 3),
        ],
    )

@pytest.fixture
def product_example2() -> Product:
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 200000.0, 5)

@pytest.fixture
def product_example3() -> Product:
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)