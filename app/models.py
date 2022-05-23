
from cProfile import label
from .database import Base
from sqlalchemy import Column, Integer,String, Boolean, Float
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

class Post(Base):
    __tablename__ = 'predictions'

    id = Column(Integer, primary_key=True, nullable=False)
    input = Column(String, nullable=False)
    label = Column(String, nullable=False)
    prediction = Column(Float, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

