import pytest
from unittest.mock import AsyncMock
from application.models import ProductNotFoundError
from application.services import (
    search_by_name,
    filter_by_category,
    find_most_expensive_product,
    calculate_total_stock_value,
    find_lowest_quantity_product,
    fetch_external_supplier_price,
)

def test_search_by_name(sample_products):
    results = search_by_name(sample_products, "Laptop")
    assert len(results) == 1
    assert results[0].name == "Laptop Lenovo"

def test_filter_by_category(sample_products):
    results = filter_by_category(sample_products, "Peripherals")
    assert len(results) == 2

def test_find_most_expensive_product(sample_products):
    product = find_most_expensive_product(sample_products)
    assert product.name == "Laptop Lenovo"
    assert product.price == pytest.approx(25000.0)

def test_find_most_expensive_product_empty_raises(empty_catalog):
    with pytest.raises(ProductNotFoundError):
        find_most_expensive_product(empty_catalog)

def test_calculate_total_stock_value(sample_products):
    total = calculate_total_stock_value(sample_products)
    # (25000*10) + (800*50) + (2500*20) + (18000*15) = 250000 + 40000 + 50000 + 270000 = 610000
    assert total == pytest.approx(610000.0)

def test_calculate_total_stock_value_empty(empty_catalog):
    assert calculate_total_stock_value(empty_catalog) == pytest.approx(0.0)

def test_find_lowest_quantity_product(sample_products):
    product = find_lowest_quantity_product(sample_products)
    assert product.name == "Laptop Lenovo"
    assert product.quantity == 10

def test_find_lowest_quantity_product_empty_raises(empty_catalog):
    with pytest.raises(ProductNotFoundError):
        find_lowest_quantity_product(empty_catalog)

@pytest.mark.asyncio
async def test_fetch_external_supplier_price_async():
    price = await fetch_external_supplier_price("Smartwatch")
    assert price == pytest.approx(1500.0)

@pytest.mark.asyncio
async def test_fetch_external_supplier_price_mock():
    mock_service = AsyncMock(return_value=1200.0)
    price = await mock_service("Smartwatch")
    assert price == pytest.approx(1200.0)
    mock_service.assert_called_once_with("Smartwatch")

@pytest.mark.asyncio
async def test_fetch_external_supplier_price_failure():
    mock_service = AsyncMock(side_effect=ValueError("Service unavailable"))
    with pytest.raises(ValueError, match="Service unavailable"):
        await mock_service("Smartwatch")