from dataclasses import dataclass

class InvalidProductDataError(Exception):
    """Кастомне виключення для некоректних даних товару."""
    pass

class ProductNotFoundError(Exception):
    """Кастомне виключення, коли товар не знайдено."""
    pass

@dataclass
class Product:
    name: str
    category: str
    price: float
    quantity: int

    def __post_init__(self):
        if not self.name or not self.category:
            raise InvalidProductDataError("Name and category cannot be empty.")
        if self.price < 0:
            raise InvalidProductDataError(f"Invalid price: {self.price}")
        if self.quantity < 0:
            raise InvalidProductDataError(f"Invalid quantity: {self.quantity}")