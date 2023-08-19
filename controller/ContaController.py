from flask import Flask, request, jsonify, abort
import os
import sys
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(diretorio_atual))
from domain.Transaction import Transaction


app = Flask(__name__)

transaction = Transaction()


class ContaController:


    @app.route('/saldo')
    def consulta_saldo():
        titular = request.args.get('titular')  
        if titular:
            saldo = transaction.consulta_saldo(titular)
            if not saldo:
                abort(404, "Saldo não encontrado.")
            return jsonify({"mensagem": f"O saldo de '{titular}' é {saldo}."})
        else:
            abort(400, "Parâmetro ausente na requisição.")


    @app.route('/create/poupanca',  methods = ['POST'])
    def create_popanca():
        titular = request.args.get('titular')  
        if titular:
            saldo = transaction.create_poupanca(titular,1)
            return jsonify({"mensagem": f"OK"})
        else:
            abort(400, "Parâmetro ausente na requisição.")

    
    @app.route('/create/conta',  methods = ['POST'])
    def create_conta():
        titular = request.args.get('titular')  
        if titular:
            saldo = transaction.create_conta(titular,1000)
            return jsonify({"mensagem": f"Created"})
        else:
            abort(400, "Parâmetro ausente na requisição.")

    @app.route('/create/credit',  methods = ['POST'])
    def create_transaction():
        titular = request.args.get('titular')  
        value = request.args.get('valor')  
        data = request.args.get('data')
        description = request.args.get('description')
        deposito = request.args.get('deposito')
        is_deposito = "sim" in deposito
        if titular:
            transaction.create_extrato(titular, float(value), data, description, is_deposito)
            return jsonify({"mensagem": f"OK"})
        else:
            abort(400, "Parâmetro ausente na requisição.")

    @app.route('/extrato')
    def consulta_extrato():
        titular = request.args.get('titular')  
        if titular:
            extrato = transaction.consulta_extrato(titular)
            if not extrato:
                abort(404, "Extrato não encontrado.")
                
            return extrato
        else:
            abort(400, "Parâmetro ausente na requisição.")

    @app.route('/transfer/poupanca',  methods = ['POST'])
    def transfer_to_poupanca():
        titular = request.args.get('titular') 
        value = request.args.get('valor')  
        if titular:
            message = transaction.transfer_to_poupanca(titular, float(value))
            if "sucesso" not in message:
                abort(400, message)
                
            return message
        else:
            abort(400, "Parâmetro ausente na requisição.")
    

    @app.route('/transfer/conta', methods = ['POST'])
    def transfer_to_conta():
        titular = request.args.get('titular') 
        value = request.args.get('valor')  
        if titular:
            message = transaction.transfer_to_conta(titular, float(value))
            if "sucesso" not in message:
                abort(400, message)
                
            return message
        else:
            abort(400, "Parâmetro ausente na requisição.")
    
