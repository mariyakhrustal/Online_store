def test_product_init(product_example):
    """Инициализация объектов класса Product"""
    assert product_example.name == "bottle"
    assert product_example.description == "plastic"
    assert product_example.price == 100.0
    assert product_example.quantity == 2
