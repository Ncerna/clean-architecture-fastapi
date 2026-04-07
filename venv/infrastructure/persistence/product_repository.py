from domain.repositories.i_product_repository import IProductRepository
from infrastructure.storage.product_storage import ProductStorage

class ProductRepository(IProductRepository):

    def __init__(self, storage: ProductStorage):
        self.storage = storage


    def save(self, product):

        self.storage.add(product)

    def get_by_id(self, product_id: int):
        return self.storage.get_by_id(product_id)

    def get_all(self):
        return self.storage.get_all()

    def update(self, product):
        existing = self.storage.get_by_id(product.id)
        if existing:
            existing.name = product.name
            existing.price = product.price
            existing.stock = product.stock

    def delete(self, product_id: int):
        self.storage.delete(product_id)
    
    def get_by_name(self, name: str):
        return self.storage.get_by_name(name)
    