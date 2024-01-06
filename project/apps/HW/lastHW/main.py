from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from databases import Database
from pydantic import BaseModel
from datetime import datetime

DATABASE_URL = "sqlite:/// main.db"





database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Модели таблиц


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    item_id = Column(Integer, ForeignKey("items.id"))
    order_date = Column(DateTime, default=datetime.utcnow)
    status = Column(String)


Base.metadata.create_all(bind=engine)
app = FastAPI()

# Pydantic модели для запросов и ответов


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str


class ItemCreate(BaseModel):
    name: str
    description: str
    price: float


class ItemResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float


class OrderCreate(BaseModel):
    user_id: int
    item_id: int
    status: str


class OrderResponse(BaseModel):
    id: int
    user_id: int
    item_id: int
    order_date: datetime
    status: str

# CRUD операции


async def create_user(user: UserCreate):
    query = User.__table__.insert().values(**user.dict())
    user_id = await database.execute(query)
    return {"id": user_id, **user.dict()}


async def get_user(user_id: int):
    query = User.__table__.select().where(User.id == user_id)
    return await database.fetch_one(query)


async def update_user(user_id: int, updated_user: UserCreate):
    query = User.__table__.update().whe2222testre(
        User.id == user_id).values(**updated_user.dict())
    await database.execute(query)
    return {"id": user_id, **updated_user.dict()}


async def delete_user(user_id: int):
    query = User.__table__.delete().where(User.id == user_id)
    await database.execute(query)
    return {"message": "User deleted successfully"}


async def create_item(item: ItemCreate):
    query = Item.__table__.insert().values(**item.dict())
    item_id = await database.execute(query)
    return {"id": item_id, **item.dict()}


async def get_item(item_id: int):
    query = Item.__table__.select().where(Item.id == item_id)
    return await database.fetch_one(query)


async def update_item(item_id: int, updated_item: ItemCreate):
    query = Item.__table__.update().where(
        Item.id == item_id).values(**updated_item.dict())
    await database.execute(query)
    return {"id": item_id, **updated_item.dict()}


async def delete_item(item_id: int):
    query = Item.__table__.delete().where(Item.id == item_id)
    await database.execute(query)
    return {"message": "Item deleted successfully"}


async def create_order(order: OrderCreate):
    query = Order.__table__.insert().values(**order.dict())
    order_id = await database.execute(query)
    return {"id": order_id, **order.dict()}


async def get_order(order_id: int):
    query = Order.__table__.select().where(Order.id == order_id)
    return await database.fetch_one(query)


async def update_order(order_id: int, updated_order: OrderCreate):
    query = Order.__table__.update().where(
        Order.id == order_id).values(**updated_order.dict())
    await database.execute(query)
    return {"id": order_id, **updated_order.dict()}


async def delete_order(order_id: int):
    query = Order.__table__.delete().where(Order.id == order_id)
    await database.execute(query)
    return {"message": "Order deleted successfully"}

# Маршруты


@app.post("/users/", response_model=UserResponse)
async def create_user_route(user: UserCreate):
    return await create_user(user)


@app.get("/users/{user_id}", response_model=UserResponse)
async def read_user_route(user_id: int):
    return await get_user(user_id)


@app.put("/users/{user_id}", response_model=UserResponse)
async def update_user_route(user_id: int, updated_user: UserCreate):
    return await update_user(user_id, updated_user)


@app.delete("/users/{user_id}", response_model=dict)
async def delete_user_route(user_id: int):
    return await delete_user(user_id)


@app.post("/items/", response_model=ItemResponse)
async def create_item_route(item: ItemCreate):
    return await create_item(item)


@app.get("/items/{item_id}", response_model=ItemResponse)
async def read_item_route(item_id: int):
    return await get_item(item_id)


@app.put("/items/{item_id}", response_model=ItemResponse)
async def update_item_route(item_id: int, updated_item: ItemCreate):
    return await update_item(item_id, updated_item)


@app.delete("/items/{item_id}", response_model=dict)
async def delete_item_route(item_id: int):
    return await delete_item(item_id)


@app.post("/orders/", response_model=OrderResponse)
async def create_order_route(order: OrderCreate):
    return await create_order(order)


@app.get("/orders/{order_id}", response_model=OrderResponse)
async def read_order_route(order_id: int):
    return await get_order(order_id)


@app.put("/orders/{order_id}", response_model=OrderResponse)
async def update_order_route(order_id: int, updated_order: OrderCreate):
    return await update_order(order_id, updated_order)


@app.delete("/orders/{order_id}", response_model=dict)
async def delete_order_route(order_id: int):
    return await delete_order(order_id)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
