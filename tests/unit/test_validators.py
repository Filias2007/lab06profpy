import pytest
from application.models import Product, InvalidProductDataError

@pytest.mark.parametrize(
    ("name", "category", "price", "quantity"),
    [
        ("", "Electronics", 100.0, 10),
        ("Phone", "", 100.0, 10),
        ("Phone", "Electronics", -50.0, 10),
        ("Phone", "Electronics", 100.0, -5),
    ],
)
def test_invalid_product_data_raises_exception(name, category, price, quantity):
    with pytest.raises(InvalidProductDataError):
        Product(name=name, category=category, price=price, quantity=quantity)