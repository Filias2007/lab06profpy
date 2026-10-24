import pytest
from application.exporters import CSVExporter, CSVImporter, JSONExporter
from application.models import InvalidProductDataError
from application.services import filter_by_category, calculate_total_stock_value

def test_csv_export_import_integration(tmp_path, sample_products):
    file_path = tmp_path / "products.csv"
    CSVExporter.export_to_file(sample_products, file_path)
    assert file_path.exists()

    imported_products = CSVImporter.import_from_file(file_path)
    assert len(imported_products) == len(sample_products)
    assert imported_products[0].name == sample_products[0].name
    assert imported_products[0].price == pytest.approx(sample_products[0].price)

def test_csv_import_malformed_record_raises(tmp_path):
    file_path = tmp_path / "malformed.csv"
    file_path.write_text("name,category,price,quantity\nLaptop,Electronics,INVALID_PRICE,10", encoding="utf-8")
    with pytest.raises(InvalidProductDataError):
        CSVImporter.import_from_file(file_path)

def test_json_export_integration(tmp_path, sample_products):
    file_path = tmp_path / "products.json"
    JSONExporter.export_to_file(sample_products, file_path)
    assert file_path.exists()
    assert file_path.stat().st_size > 0

def test_full_data_pipeline(tmp_path, sample_products):
    csv_file = tmp_path / "pipeline.csv"
    CSVExporter.export_to_file(sample_products, csv_file)

    loaded_products = CSVImporter.import_from_file(csv_file)
    electronics = filter_by_category(loaded_products, "Electronics")
    total_val = calculate_total_stock_value(electronics)

    assert len(electronics) == 2
    assert total_val == pytest.approx(520000.0)