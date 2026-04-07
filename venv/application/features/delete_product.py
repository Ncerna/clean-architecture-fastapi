from application.wrappers.response import Response

class DeleteProduct:

    def __init__(self, repository):
        self.repository = repository

    def execute(self, product_id: int):

        product = self.repository.get_by_id(product_id)

        if not product:
            return Response.fail("Product not found")

        self.repository.delete(product_id)

        return Response.ok(message="Product deleted successfully")