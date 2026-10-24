import os

class Config:
    MIN_STOCK_THRESHOLD = int(os.getenv("MIN_STOCK_THRESHOLD", "1"))
    MAX_PRICE_LIMIT = float(os.getenv("MAX_PRICE_LIMIT", "500000.0"))

    @classmethod
    def validate_product(cls, quantity: int, price: float) -> bool:
        return quantity >= cls.MIN_STOCK_THRESHOLD and price <= cls.MAX_PRICE_LIMIT

AppConfig = Config

def get_config():
    return Config()