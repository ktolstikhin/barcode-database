from sqlalchemy import Column, Integer, String

from .base import ModelBase


class Product(ModelBase):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    code = Column(String, nullable=False)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    brand = Column(String, nullable=False)

    def __repr__(self):
       return '<Product(code="{c}", name="{n}", brand="{b}")>'.format(
               c=self.code, n=self.name, b=self.brand)

