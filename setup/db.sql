-- Cria o banco de dados
CREATE DATABASE mydatabase;

-- Usa o banco de dados recém-criado
USE mydatabase;

-- Cria a tabela 'conta'
CREATE TABLE conta (
    id INT PRIMARY KEY,
    titular VARCHAR(100),
    saldo INT,
    tipo VARCHAR(50)
);

-- Cria a tabela 'poupanca' com relação de herança
CREATE TABLE poupanca (
    id INT PRIMARY KEY,
    FOREIGN KEY (id) REFERENCES conta(id)
);

-- Cria a tabela 'extrato'
CREATE TABLE extrato (
    id INT PRIMARY KEY,
    data DATE,
    description VARCHAR(255),
    value_transaction FLOAT,
    conta_id INT,
    FOREIGN KEY (conta_id) REFERENCES conta(id)
);
