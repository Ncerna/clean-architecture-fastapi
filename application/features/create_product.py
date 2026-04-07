from domain.entities.product import Product
from fastapi import HTTPException, status
from domain.value_objects.product_name import ProductName
from domain.value_objects.price import Price
from domain.value_objects.stock import Stock
from application.repositories.i_product_repository import IProductRepository
from application.dtos.product_dto import ProductDTO
from application.wrappers.response import Response

class CreateProduct:

    def __init__(self, repository: IProductRepository):
        self.repository = repository

    def execute(self, dto: ProductDTO):
        existing = self.repository.get_by_name(dto.name)

        if existing:
            print("ENTRÓ AL IF")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Product name already exists"
            )
        product = Product(
            product_id=dto.id,
            name=ProductName(dto.name),
            price=Price(dto.price),
            stock=Stock(dto.stock)
        )

        self.repository.save(product)

        return Response.ok(
            data={
                "id": product.id,
                "name": product.name.value,
                "price": product.price.value,
                "stock": product.stock.value
            },
            message="Product created successfully"
        )
   