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
