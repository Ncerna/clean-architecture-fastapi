from application.wrappers.response import Response
from application.repositories.i_product_repository import IProductRepository

class GetProducts:

    def __init__(self, repository):
        self.repository = repository

    def execute(self):
        try:
            products = self.repository.get_all()
            print(f"Products: {len(products)}")
            data = [
                {
                    "id": p.id,
                    "name": p.name.value,
                    "price": p.price.value,
                    "stock": p.stock.value
                }
                for p in products
            ]

            return Response.ok(data=data)

        except Exception as e:
          
            return Response.fail(f"Error getting products: {str(e)}")