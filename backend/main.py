from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import List, Optional

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str 
    style: str 
    material: str 
    price: float
    in_stock: bool = Field(default=True)

sqlite_url = "sqlite:///database.db"
engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})

def create_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

app = FastAPI(title="Mini Home Catalog API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    create_tables()

@app.post("/api/products", response_model=Product)
def add_product(product: Product, session: Session = Depends(get_session)):
    try:
        session.add(product)
        session.commit()
        session.refresh(product)
        return product
    except Exception:
        session.rollback()
        raise HTTPException(status_code=400, detail="Invalid product data provided.")

@app.get("/api/products", response_model=List[Product])
def get_all_products(session: Session = Depends(get_session)):
    products = session.exec(select(Product)).all()
    return products

@app.delete("/api/products/{product_id}")
def delete_product(product_id: int, session: Session = Depends(get_session)):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found.")
    session.delete(product)
    session.commit()
    return {"message": "Product deleted successfully."}