from flask import Flask, request, jsonify, abort
import os
import sys
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(diretorio_atual))
from domain.Transaction import Transaction
from flask_sqlalchemy import SQLAlchemy
import json



app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///transactions.db'
# db = SQLAlchemy(app)
# # Importe seus modelos aqui (após a criação do objeto db)
# from domain.model.Conta import Conta  
# # Crie as tabelas aqui, dentro do contexto de aplicativo
# with app.app_context():
#     db.create_all()

transaction = Transaction()


@app.route('/conta/')
class ContaController:


    @app.route('/saldo/')
    def consulta_saldo():
        titular = request.args.get('titular')  # Obtém o valor do parâmetro da URL
        if titular:
            saldo = transaction.consulta_saldo(titular)
            if not saldo:
                abort(404, "Saldo não encontrado.")
            saldo = 0
            return jsonify({"mensagem": f"O saldo de '{titular}' é {saldo}."})
        else:
            abort(400, "Parâmetro ausente na requisição.")


    @app.route('/create/poupanca',  methods = ['POST'])
    def create_popanca():
        titular = request.args.get('titular')  # Obtém o valor do parâmetro da URL
        if titular:
            saldo = transaction.create_pupanca(titular,1)
            return jsonify({"mensagem": f"OK"})
        else:
            abort(400, "Parâmetro ausente na requisição.")

    
    @app.route('/create/conta/',  methods = ['POST'])
    def create_conta():
        titular = request.args.get('titular')  # Obtém o valor do parâmetro da URL
        if titular:
            saldo = transaction.create_conta(titular,1000)
            return jsonify({"mensagem": f"Created"})
        else:
            abort(400, "Parâmetro ausente na requisição.")

    @app.route('/create/credit/',  methods = ['POST'])
    def create_transaction():
        titular = request.args.get('titular')  # Obtém o valor do parâmetro da URL
        value = request.args.get('valor')  # Obtém o valor do parâmetro da URL
        data = request.args.get('data')
        description = request.args.get('description')
        if titular:
            transaction.create_extrato(titular, value, data, description)
            return jsonify({"mensagem": f"OK"})
        else:
            abort(400, "Parâmetro ausente na requisição.")

    @app.route('/extrato/')
    def consulta_extrato():
        titular = request.args.get('titular')  # Obtém o valor do parâmetro da URL
        if titular:
            extrato = transaction.consulta_extrato(titular)
            if not extrato:
                abort(404, "Extrato não encontrado.")
                
            return extrato
        else:
            abort(400, "Parâmetro ausente na requisição.")

    @app.route('/transfer/poupanca/',  methods = ['POST'])
    def transfer_to_poupanca(titular, value):
        pass

    @app.route('/transfer/conta/', methods = ['POST'])
    def transfer_to_conta(titular, value):
        pass

if __name__ == '__main__':
    app.run()