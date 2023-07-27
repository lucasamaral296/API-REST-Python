from flask import Flask

app = Flask(__name__)  # Cria o Site    

@app.route("/")   # decorator  -  Diz em qual link a função vai rodar
def hello_world():  # função
    return {"Lucas": "Dev em Crescimento"}

@app.route("/teste")   # decorator  -  Diz em qual link a função vai rodar
def teste():  # função
    return {"Teste": "Em Andamento"}

@app.route("/outroteste")   # decorator  -  Diz em qual link a função vai rodar
def outroteste():  # função
    return {"Outro Teste": "Em Andamento Tambem", "Nome": "Lucas", "Dev": "Python"}

app.run(debug=True)  # coloca o site no ar