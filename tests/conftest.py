import pytest
from application.models import Product
from application.repositories import InMemoryRepository

@pytest.fixture
def sample_products():
    return [
        Product(name="Laptop Lenovo", category="Electronics", price=25000.0, quantity=10),
        Product(name="Wireless Mouse", category="Peripherals", price=800.0, quantity=50),
        Product(name="Gaming Keyboard", category="Peripherals", price=2500.0, quantity=20),
        Product(name="Smartphone Samsung", category="Electronics", price=18000.0, quantity=15),
    ]

@pytest.fixture
def empty_catalog():
    return []

@pytest.fixture
def product_repository(sample_products):
    repo = InMemoryRepository[Product]()
    for idx, product in enumerate(sample_products):
        repo.add(f"product_{idx}", product)
    return repo