from domain.value_objects.product_name import ProductName
from domain.value_objects.price import Price
from domain.value_objects.stock import Stock

class Product:
    def __init__(self, product_id: int, name: ProductName, price: Price, stock: Stock):
        self.id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def update_price(self, new_price: Price):
        self.price = new_price

    def increase_stock(self, quantity: int):
        self.stock = Stock(self.stock.value + quantity)