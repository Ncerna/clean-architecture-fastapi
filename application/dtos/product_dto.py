class ProductDTO:
    def __init__(self, id: int = None, name: str = None, price: float = None, stock: int = None):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock