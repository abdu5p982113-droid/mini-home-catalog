from sqlmodel import SQLModel, Field
from typing import Optional

class Furniture(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str      
    category: str  
    material: str  
    price: float