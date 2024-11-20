from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Promo(Base):
    __tablename__ = "promos"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code = Column(String(100), index=True, nullable=False)
    expiration_date = Column(DATETIME, index=True, nullable=False)