from application.wrappers.response import Response
from application.repositories.i_product_repository import IProductRepository

class GetProductById:

    def __init__(self, repository):
        self.repository = repository

    def execute(self, product_id: int):

        product = self.repository.get_by_id(product_id)

        if not product:
            return Response.fail("Product not found")

        data = {
            "id": product.id,
            "name": product.name.value,
            "price": product.price.value,
            "stock": product.stock.value
        }

        return Response.ok(data=data)