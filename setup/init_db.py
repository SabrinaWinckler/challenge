import os
import sys
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(diretorio_atual))

from domain.Transaction import Transaction

t = Transaction()

def criar_registros():
    t.create_conta("João",1000)
    t.create_extrato("João")
    

if __name__ == '__main__':
    criar_registros()
