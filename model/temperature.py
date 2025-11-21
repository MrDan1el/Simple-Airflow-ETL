from sqlalchemy import Column, Integer, VARCHAR, Float, TIMESTAMP
import sys
sys.path.append("..")
from model.base import Base


class Temperature(Base):
    __tablename__ = 'city_temperature'
    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    city = Column(VARCHAR(50), nullable=False)
    l_time = Column(TIMESTAMP, nullable=False, index=True)
    temp = Column(Float, nullable=False)