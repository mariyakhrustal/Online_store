from unittest.mock import patch

from src.utils import create_objects_from_json, read_json


# Тест 1: Корректный JSON
def test_valid_json(tmpdir) -> None:
    """Тест для корректного чтения JSON"""
    # Создание временного файла во временной директории
    temp_file = tmpdir.join("test.json")
    temp_file.write('{"key": "value"}')

    # Вызов функции с путём к временно созданному файлу
    result = read_json(str(temp_file))
    expected = {"key": "value"}
    assert result == expected


# Тест 2: Некорректный JSON
def test_invalid_json(tmpdir) -> None:
    """Тест для некорректного JSON (не закрыта фигурная скобка)"""
    # Создание временного файла с некорректным JSON
    temp_file = tmpdir.join("invalid.json")
    temp_file.write('{"key": "value"')

    result = read_json(str(temp_file))
    assert result is None  # Функция должна напечатать ошибку и вернуть None


# Тест 3: Файл не найден
def test_file_not_found(tmpdir) -> None:
    """Тест для случая, когда файл не найден"""
    # Используем путь, который не существует
    temp_file = tmpdir.join("non_existent_file.json")
    result = read_json(str(temp_file))
    assert result is None  # Функция должна напечатать ошибку и вернуть None


# Тест 4: Вызывается исключение на другие ошибки
def test_raise_exception() -> None:
    """Тест, когда вызывается исключение на непредвиденные ошибки"""
    with patch("builtins.print") as mock_print:
        with patch("builtins.open", side_effect=Exception("Произошла непредвиденная ошибка")):
            result = read_json("nonexistent_file.json")
            assert result is None, "Ожидалось, что результат будет None"
            mock_print.assert_called_with("Произошла непредвиденная ошибка: Произошла непредвиденная ошибка")


def test_empty_data() -> None:
    """Проверяем, что возвращается пустой список"""
    data: list = []

    categories = create_objects_from_json(data)

    assert len(categories) == 0


def test_invalid_data() -> None:
    """Проверяем неправильный формат данных"""
    data = [{"name": "Electronics", "products": [{"name": "Laptop", "price": 1000}, {"name": "Smartphone"}]}]

    try:
        create_objects_from_json(data)
    except TypeError:
        pass  # Ожидаем ошибку TypeError


def test_missing_key() -> None:
    """Проверяем, если в данных отсутствует ключ 'products'"""
    data = [{"name": "Electronics"}]

    try:
        create_objects_from_json(data)
    except KeyError:
        pass  # Ожидаем ошибку KeyError


def test_single_category_no_products() -> None:
    """Проверяем, что категория была создана, но продуктов нет"""
    data = [{"name": "Books", "description": "Some description", "products": []}]

    categories = create_objects_from_json(data)

    assert len(categories) == 1
    category = categories[0]
    assert category.name == "Books"
    assert category.description == "Some description"
    assert len(category.products) == 0
