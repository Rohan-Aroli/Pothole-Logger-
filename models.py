from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime
from db import Base

class Pothole(Base):
    __tablename__ = "potholes_ml"

    id = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float)
    longitude = Column(Float)
    severity = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)