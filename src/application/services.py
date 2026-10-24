import asyncio
from typing import List
from application.models import Product, ProductNotFoundError, InvalidProductDataError
from application.config import Config

def add_product(catalog: List[Product], product: Product) -> None:
    if not Config.validate_product(product.quantity, product.price):
        raise InvalidProductDataError("Product does not meet configuration limits.")
    catalog.append(product)

def search_by_name(catalog: List[Product], name: str) -> List[Product]:
    return [p for p in catalog if name.lower() in p.name.lower()]

def filter_by_category(catalog: List[Product], category: str) -> List[Product]:
    return [p for p in catalog if p.category.lower() == category.lower()]

def find_most_expensive_product(catalog: List[Product]) -> Product:
    if not catalog:
        raise ProductNotFoundError("Catalog is empty.")
    return max(catalog, key=lambda p: p.price)

def calculate_total_stock_value(catalog: List[Product]) -> float:
    if not catalog:
        return 0.0
    return sum(p.price * p.quantity for p in catalog)

def find_lowest_quantity_product(catalog: List[Product]) -> Product:
    if not catalog:
        raise ProductNotFoundError("Catalog is empty.")
    return min(catalog, key=lambda p: p.quantity)

async def fetch_external_supplier_price(product_name: str) -> float:
    await asyncio.sleep(0.01)
    if not product_name:
        raise ValueError("Product name is required")
    return 1500.0