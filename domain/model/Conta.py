from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, relationship
from setup.config import Base, SessionLocal
from domain.model.Extrato import Extrato


class Conta(Base):
    __tablename__ = 'conta'

    id = Column(Integer, primary_key=True)
    titular = Column(String)
    saldo =  Column(Float)
    extrato = relationship('Extrato', back_populates='conta')


    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo


    
