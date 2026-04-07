from fastapi import FastAPI

from presentation.controllers.product_controller import router as product_router

app = FastAPI(
    title="API",
    version="1.0.0"
)

# registrar rutas
app.include_router(product_router, prefix="/products")



