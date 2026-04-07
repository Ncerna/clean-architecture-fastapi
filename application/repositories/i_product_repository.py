from abc import ABC, abstractmethod
from domain.entities.product import Product

class IProductRepository(ABC):

    @abstractmethod
    def save(self, product: Product):
        pass

    @abstractmethod
    def get_by_id(self, product_id: int):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, product: Product):
        pass

    @abstractmethod
    def delete(self, product_id: int):
        pass
   
    @abstractmethod
    def get_by_name(self, name: str):
        pass