from fastapi import APIRouter

from presentation.schemas.product_schema import ProductCreateRequest
from application.dtos.product_dto import ProductDTO

from application.features.create_product import CreateProduct
from application.features.get_products import GetProducts
from application.features.get_product_by_id import GetProductById
from application.features.delete_product import DeleteProduct

from infrastructure.persistence.product_repository import ProductRepository
from infrastructure.storage.product_storage import ProductStorage

router = APIRouter()

# -------------------------
# INFRA SETUP (simple DI)
# -------------------------
storage = ProductStorage()
repository = ProductRepository(storage)

# Use cases
create_product = CreateProduct(repository)
get_products = GetProducts(repository)
get_product_by_id = GetProductById(repository)
delete_product = DeleteProduct(repository)

@router.post("")
def create(request: ProductCreateRequest):

    dto = ProductDTO(
        id=request.id,
        name=request.name,
        price=request.price,
        stock=request.stock
    )

    result = create_product.execute(dto)
    return result.data



@router.get("")
def get_all():
    result = get_products.execute()
    return result.data


@router.get("/{product_id}")
def get_by_id(product_id: int):
    result = get_product_by_id.execute(product_id)
    return result.data



@router.delete("/{product_id}")
def delete(product_id: int):
    result = delete_product.execute(product_id)
    return result.data