import os
import sys
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(diretorio_atual))

from domain.Transaction import Transaction

t = Transaction()

def criar_registros():
    t.create_conta("Fulano",1000)
    t.create_poupanca("Fulano",1)
    t.create_extrato("Fulano")
