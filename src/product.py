class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        self.__price = new_price

    @classmethod
    def new_product(cls, new_product: dict, products: list) -> "Product":
        """Взвращает созданный объект класса Product из параметров товара в словаре"""
        name = new_product["name"]
        description = new_product["description"]
        price = new_product["price"]
        quantity = new_product["quantity"]
        existing_product = next((product for product in products if product.name == name), None)
        if existing_product:
            existing_product.quantity += quantity
            existing_product.price = max(existing_product.price, price)
            return existing_product
        else:
            new_product_obj = cls(name, description, price, quantity)
            products.append(new_product_obj)
            return new_product_obj
