from sqlalchemy.orm import Session
from models import Product, Order, OrderItem
from schemas import ProductCreate, ProductUpdate, OrderCreate, OrderUpdate

def create_product(db: Session, product: ProductCreate):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def update_product(db: Session, product_id: int, product: ProductUpdate):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product:
        for key, value in product.dict(exclude_unset=True).items():
            setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product

def create_order(db: Session, order: OrderCreate):
    db_order = Order(customer_id=order.customer_id)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    
    for product_id in order.product_ids:
        db_order_item = OrderItem(order_id=db_order.id, product_id=product_id)
        db.add(db_order_item)

    db.commit()
    return db_order

def get_order(db: Session, order_id: int):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        return None
    product_ids = [item.product_id for item in db.query(OrderItem).filter(OrderItem.order_id == order.id).all()]
    return {
        "id": order.id,
        "customer_id": order.customer_id,
        "status": order.status,
        "product_ids": product_ids
    }


def update_order_status(db: Session, order_id: int, order: OrderUpdate):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if not db_order:
        return None
    
    db_order.status = order.status
    db.commit()
    db.refresh(db_order)

    product_ids = [item.product_id for item in db.query(OrderItem).filter(OrderItem.order_id == db_order.id).all()]

    return {
        "id": db_order.id,
        "customer_id": db_order.customer_id,
        "status": db_order.status,
        "product_ids": product_ids
    }


def delete_order(db: Session, order_id: int):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    
    if not db_order:
        return None
    
    db.query(OrderItem).filter(OrderItem.order_id == order_id).delete()
    
    db.delete(db_order)
    db.commit()
    
    return db_order

