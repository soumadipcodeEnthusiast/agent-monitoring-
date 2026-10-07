from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float, Boolean, JSON, ForeignKey, DateTime
from datetime import datetime

Base = declarative_base()

class Agent(Base):
    __tablename__ = 'agents'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
