from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DateTime
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Review(Base):
    __tablename__ = "ReviewSystem"

    id = Column(Integer, primary_key=True, autoincrement=True)
    message = Column(String(300), nullable=False)
    score = Column(Integer, nullable=False)
