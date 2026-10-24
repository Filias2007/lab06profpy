import pytest
from application.models import Product, InvalidProductDataError

def test_product_creation_valid():
    p = Product(name="Monitor LG", category="Electronics", price=7500.0, quantity=8)
    assert p.name == "Monitor LG"
    assert p.category == "Electronics"
    assert p.price == pytest.approx(7500.0)
    assert p.quantity == 8

def test_repository_add_and_get(product_repository):
    all_items = product_repository.list_all()
    assert len(all_items) == 4
    retrieved = product_repository.get_by_key("product_0")
    assert retrieved is not None
    assert retrieved.name == "Laptop Lenovo"