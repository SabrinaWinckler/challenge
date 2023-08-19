# challenge

## Setup enviroment

Install python dependencies
```shell script
pip install -r requiremtens.txt
```

## Run Application
```shell script
python app.py 
```

For create accounts and fake transactions you can use:

- Create Conta:
    Conta always will be created with saldo 1000

```shell script
curl --location --request POST 'http://127.0.0.1:5000/create/conta?titular=Maria'
```
- Create Poupança:
    Poupança  always will be created with saldo 1

```shell script
curl --location --request POST 'http://127.0.0.1:5000/create/poupanca?titular=Maria'
```
- Create Extrato:
    Date format required is %Y-%m-%d 
    And if is deposito you need to set parameter with sim 
    The default values are data today and is deposito false

```shell script
curl --location --request POST 'http://127.0.0.1:5000/create/credit?titular=Maria&valor=1&data=null&description=null&deposito=null'
```

If you prefer you can use titular named "Fulano" for make your tests

## For execute A scope
The params are:
- titular

```shell script
curl --location 'http://127.0.0.1:5000/saldo?titular=Maria'
```

## For execute B scope
The params are:
- titular

```shell script
curl --location 'http://127.0.0.1:5000/extrato?titular=Maria'
```

## For execute C scope
The params are:
- titular
- valor (that determines how much you want to invest, limites by the saldo in you conta) 

```shell script
curl --location --request POST 'http://127.0.0.1:5000/transfer/poupanca?titular=Maria&valor=5'
```

## For execute D scope
The params are:
- titular
- valor (that determines how much you want to save, limites by the saldo in you poupança) 

```shell script
curl --location --request POST 'http://127.0.0.1:5000/transfer/conta?titular=Maria&valor=4'
```

## Run Tests
```shell script
python .\test\TransactionTest.py 
```


## Related Docs