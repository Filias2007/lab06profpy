# Lab 06: Automated Testing for E-Commerce System (Variant 3)

Проєкт містить доменну модель, бізнес-логіку та повноцінний набір автоматизованих тестів (`pytest`) для системи «Інтернет-магазин» (E-Commerce Processing System).

## 📁 Структура проєкту

- `src/application/` — основний код застосунку:
  - `models.py` — доменні сутності (`Product`), винятки (`InvalidProductDataError`, `ProductNotFoundError`).
  - `config.py` — налаштування середовища та конфігурація валідації.
  - `repositories.py` — універсальне сховище даних у пам'яті (`InMemoryRepository`).
  - `services.py` — бізнес-логіка (пошук, фільтрація, розрахунок вартості) та асинхронні виклики.
  - `exporters.py` — імпорт та експорт даних у формати CSV та JSON.
- `tests/` — набір автоматизованих тестів:
  - `conftest.py` — спільні фікстури Pytest (`sample_products`, `empty_catalog`, `product_repository`).
  - `unit/` — модульні тести моделей, валідаторів та сервісів (`Mock`, `AsyncMock`).
  - `integration/` — інтеграційні тести конфігурації (`monkeypatch`) та файлового імпорту/експорту (`tmp_path`).

## 🚀 Налаштування та запуск

### 1. Створення та активація віртуального середовища
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1