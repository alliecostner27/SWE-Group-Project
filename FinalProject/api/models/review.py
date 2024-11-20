from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Review(Base):
    __tablename__ = "ReviewSystem"

    id = Column(Integer, primary_key=True, autoincrement=True)  # Primary key column
    message = Column(String(300), nullable=False)  # Example: Not null constraint
    score = Column(Integer, nullable=False)
