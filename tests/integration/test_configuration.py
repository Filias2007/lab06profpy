import pytest
from application.models import Product, InvalidProductDataError
from application.services import add_product

def test_monkeypatch_min_stock_config(monkeypatch, empty_catalog):
    monkeypatch.setattr("application.config.Config.MIN_STOCK_THRESHOLD", 15)
    low_stock_product = Product(name="USB Cable", category="Peripherals", price=150.0, quantity=5)

    with pytest.raises(InvalidProductDataError):
        add_product(empty_catalog, low_stock_product)