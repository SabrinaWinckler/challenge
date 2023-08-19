from setup.config import Base, SessionLocal
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import sessionmaker, relationship


class Extrato(Base):
    __tablename__ = 'extrato'

    id = Column(Integer, primary_key=True)
    data = Column(Date)
    description = Column(String)
    value_transaction = Column(Float)
    conta_id = Column(Integer, ForeignKey('conta.id'))

    conta = relationship('Conta', back_populates='extrato')

    def __init__(self, data, description, value_transaction, conta):
        self.data = data
        self.description = description
        self.value_transaction = value_transaction
        self.conta_id = conta.id

    def __str__(self):
        return {"Data": {self.data.strftime('%Y-%m-%d')}, "Descrição": {self.description}, "Valor da Transação": {self.value_transaction}}