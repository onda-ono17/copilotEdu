from typing import Optional, List, Dict

class ProductService:
    def __init__(self):
        self.products = [
            {"id": 1, "name": "Laptop", "price": 1200.0, "category": "Electronics"},
            {"id": 2, "name": "Coffee Maker", "price": 80.0, "category": "Home"}
        ]

    def get_product(self, product_id: int) -> Optional[Dict]:
        for product in self.products:
            if product['id'] == product_id:
                return product
        return None

    def add_product(self, name: str, price: float, category: str) -> Dict:
        new_id = len(self.products) + 1
        new_product = {"id": new_id, "name": name, "price": price, "category": category}
        self.products.append(new_product)
        return new_product
