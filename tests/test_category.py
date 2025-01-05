def test_category_init(category_example1, category_example2):
    """Инициализация объектов класса Category"""
    assert category_example1.name == "packaging"
    assert category_example1.description == "packaging for drinks"
    assert category_example1.products == []

    assert category_example2.name == "packaging"
    assert category_example2.description == "packaging for milk"
    assert len(category_example2.products) == 3

    assert category_example1.category_count == 2
    assert category_example2.category_count == 2

    assert category_example1.product_count == 3
    assert category_example2.product_count == 3
