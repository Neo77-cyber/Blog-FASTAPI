from sqlalchemy import Column, String, Integer, DateTime
from .database import Base



class DbPost(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key = int, index = True)
    title = Column(String)
    details = Column(String)
    creator = Column(String)
    image_url = Column(String)
    timestamp = Column(DateTime)
