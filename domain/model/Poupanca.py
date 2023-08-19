from domain.model.Conta import Conta
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey


class Poupanca(Conta):
   __tablename__ = 'poupanca'
   id = Column(Integer, ForeignKey('conta.id'), primary_key=True)


   def __init__(self, titular, saldo):
      super().__init__(titular=titular, saldo=saldo)
      self.active = True
