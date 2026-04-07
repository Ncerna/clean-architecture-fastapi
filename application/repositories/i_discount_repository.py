from abc import ABC, abstractmethod

class IDiscountStrategy(ABC):

    @abstractmethod
    def calculate_discount(self, price: float) -> float:
        pass