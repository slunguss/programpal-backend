from sqlalchemy import Column, String, Integer
from database import Base
import uuid

class Program(Base):
    __tablename__ = "programs"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    days_per_week = Column(Integer, nullable=False)