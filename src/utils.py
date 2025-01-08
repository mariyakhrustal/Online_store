import json
import os
from typing import Any

from src.category import Category
from src.product import Product


def read_json(path: str) -> Any:
    """Функция для чтения данных из json файла"""
    try:
        full_path = os.path.abspath(path)
        with open(full_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: Файл {full_path} не был найден.")
    except json.JSONDecodeError:
        print(f"Error: Не удалось декодировать JSON из файла {full_path}.")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")


def create_objects_from_json(data: list[dict]) -> list:
    """Функция создает объекты из полученных данных"""
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories


if __name__ == "__main__":
    raw_data = read_json("../data/products.json")
    products_data = create_objects_from_json(raw_data)
    print(products_data)

    print(products_data[0].name)
    print(products_data[0].products)
