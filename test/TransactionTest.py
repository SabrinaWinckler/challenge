import unittest
import os
import sys
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(diretorio_atual))
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from setup.config import *
from domain.model.Conta import Conta
from domain.Transaction import Transaction
from datetime import datetime

class TestTransaction(unittest.TestCase):
    def setUp(self):
        # self.engine = create_engine('sqlite:///test_db.sqlite')  
        # SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        # self.session = SessionLocal()
        # Base.metadata.create_all(self.engine)
        self.transaction = Transaction()
        self.transaction.create_conta("Fulano",1000)
        self.transaction.create_poupanca("Fulano",1)
        self.transaction.create_extrato("Fulano",10)


    # def tearDown(self):
    #     self.transaction.session.close()
    #     self.transaction.drop_all(self.engine)

    def test_consulta_saldo(self):
        saldo = self.transaction.consulta_saldo("Fulano")
        self.assertNotEqual(saldo, 0)

    def test_consulta_saldo_not_found_titular(self):
        saldo = self.transaction.consulta_saldo("Test 2")
        self.assertEqual(saldo, None)

    
    def test_consulta_extrato(self):
        ext = self.transaction.consulta_extrato("Fulano")
        self.assertIsNotNone(ext)

    def test_consulta_extrato_not_found_titular(self):
        ext = self.transaction.consulta_extrato("Test 2")
        self.assertIsNone(ext)

    def test_transfer_poupanca(self):
        message = self.transaction.transfer_to_poupanca("Fulano",10)
        self.assertIsNotNone(message)
        self.assertTrue("sucesso" in message)

    def test_transfer_poupanca_negative_value(self):
        message = self.transaction.transfer_to_poupanca("Fulano",5000)
        self.assertIsNotNone(message)
        self.assertFalse("sucesso" in message)

    def test_transfer_conta(self):
        message = self.transaction.transfer_to_conta("Fulano",10)
        self.assertIsNotNone(message)
        self.assertTrue("sucesso" in message)

    def test_transfer_conta_negative_value(self):
        message = self.transaction.transfer_to_conta("Fulano",5000)
        self.assertIsNotNone(message)
        self.assertFalse("sucesso" in message)

if __name__ == '__main__':
    unittest.main()
