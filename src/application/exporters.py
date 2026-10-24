import csv
import json
from pathlib import Path
from typing import List
from application.models import Product, InvalidProductDataError

class CSVExporter:
    @staticmethod
    def export_to_file(products: List[Product], file_path: Path) -> None:
        with open(file_path, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["name", "category", "price", "quantity"])
            for p in products:
                writer.writerow([p.name, p.category, p.price, p.quantity])

class CSVImporter:
    @staticmethod
    def import_from_file(file_path: Path) -> List[Product]:
        products: List[Product] = []
        with open(file_path, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row_idx, row in enumerate(reader, start=2):
                try:
                    product = Product(
                        name=row["name"],
                        category=row["category"],
                        price=float(row["price"]),
                        quantity=int(row["quantity"]),
                    )
                    products.append(product)
                except (KeyError, ValueError) as e:
                    raise InvalidProductDataError(f"Malformed CSV record at line {row_idx}: {e}")
        return products

class JSONExporter:
    @staticmethod
    def export_to_file(products: List[Product], file_path: Path) -> None:
        data = [
            {
                "name": p.name,
                "category": p.category,
                "price": p.price,
                "quantity": p.quantity,
            }
            for p in products
        ]
        with open(file_path, mode="w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)