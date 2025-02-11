from fastapi import FastAPI
from routes import product_routes, order_routes
from database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="E-commerce API")

app.include_router(product_routes.router, prefix="/products", tags=["Products"])
app.include_router(order_routes.router, prefix="/orders", tags=["Orders"])
