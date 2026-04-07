class ProductName:
    def __init__(self, value: str):
        if not value or len(value) < 2:
            raise ValueError("Product name is invalid")
        self.value = value