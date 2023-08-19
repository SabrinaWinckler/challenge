from setup.config import Base, SessionLocal
from domain.model.Conta import Conta
from domain.model.Poupanca import Poupanca
from domain.model.Extrato import Extrato
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from sqlalchemy import create_engine
import json



class Transaction:
    def __init__(self) -> None:
        self.engine = create_engine('sqlite:///transactions.sqlite')  
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.session = SessionLocal()
        self.base = Base.metadata.create_all(self.engine)
        self.session = SessionLocal()

    def consulta_saldo(self, titular):
        conta = self.consulta_conta(titular)
        if conta:
            return conta.saldo
        return None

    def consulta_extrato(self, titular):
        conta = self.consulta_conta(titular)
        if conta:
            data_atual = datetime.now()
            extrato_mes = [ext.__str__() for ext in conta.extrato if ext.data.month == data_atual.month and ext.data.year == data_atual.year]
            extrato_completo = {"Titular": conta.titular,"Saldo Atual": conta.saldo, "Extrato": extrato_mes}
            return json.dumps(extrato_completo, indent=4, default=str, ensure_ascii=False)
        return None

    def transfer_to_poupanca(self, titular, saldo):
        conta = self.consulta_conta(titular)
        poupanca = self.consulta_poupanca(titular)
        if not conta:
            return None
        if conta and not poupanca:
            self.create_poupanca(titular,saldo)
        if conta.saldo >= saldo:
            self.create_extrato(titular,saldo, datetime.now().strftime('%Y-%m-%d'),"Investimento Poupança")
            poupanca.saldo = poupanca.saldo + saldo
            self.session.commit()
            message = {"Message":"Invesntimento poupança realizado com sucesso", "Saldo atual Poupança" : poupanca.saldo, "Saldo atual conta corrente": conta.saldo}
            return json.dumps(message,  ensure_ascii=False)
        
        return {"Message":"Saldo insuficiente na conta"}


    def transfer_to_conta(self, titular, saldo):
        conta = self.consulta_conta(titular)
        poupanca = self.consulta_poupanca(titular)
        if not conta:
            return None
        if conta and not poupanca:
            self.create_poupanca(titular,saldo)
        if poupanca.saldo >= saldo:
            self.create_extrato(titular,saldo, datetime.now().strftime('%Y-%m-%d'),"Resgate Poupança", True)
            poupanca.saldo = poupanca.saldo - saldo
            self.session.commit()
            message = {"Message":"Resgate poupança realizado com sucesso", "Saldo atual Poupança" : poupanca.saldo, "Saldo atual conta corrente": conta.saldo}
            return  json.dumps(message,  ensure_ascii=False)
        
        return {"Message":"Saldo insuficiente na conta"}

    def create_conta(self, titular, saldo):
        conta = Conta(titular=titular, saldo=saldo)
        self.session.add(conta)
        self.session.commit()
        self.session.close()
        return conta

    
    def create_poupanca(self,titular,saldo):
        poupanca = Poupanca(titular,saldo)
        self.session.add(poupanca)
        self.session.commit()
        self.session.close()
        return poupanca

    def create_extrato(self, titular, value=20, data="2023-8-18", description="Saque", entrada=False):
        conta = self.consulta_conta(titular)
        if entrada:
            conta.saldo  = conta.saldo + value
        else:
            conta.saldo  = conta.saldo - value
        self.session.commit()
        data_obj = datetime.strptime(data, '%Y-%m-%d')
        extrato =Extrato(data=data_obj,description=description,value_transaction=value,conta=conta)
        self.session.add(extrato)
        self.session.commit()
        return extrato

    def consulta_conta(self, titular):
        conta = self.session.query(Conta).filter_by(titular=titular).first()
        return conta

    def consulta_poupanca(self, titular):
        conta = self.session.query(Poupanca).filter_by(titular=titular).first()
        return conta