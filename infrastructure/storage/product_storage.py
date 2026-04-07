class ProductStorage:
    def __init__(self):
        self.products = []


    def add(self, product):
        self.products.append(product)

    def get_all(self):
        return self.products

    def get_by_id(self, product_id):
        for p in self.products:
            
            if p.id == product_id:
                return p
        return {
        "message": "Product not found."
        }

    def get_by_name(self, name: str):
        for product in self.products:
        
            if product.name.value.lower() == name.lower():
                print(type(product.name.value), product.name.value)
                return product
        return None

    def delete(self, product_id):
        self.products = [p for p in self.products if p.id != product_id]
        