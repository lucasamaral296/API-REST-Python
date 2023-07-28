from flask import Flask
import pandas as pd

app = Flask(__name__)  # Cria o Site   
tabela = pd.read_excel('Vendas - Dez.xlsx')

@app.route("/")   # decorator  -  Diz em qual link a função vai rodar
def fat():  # função
  faturamento = float(tabela["Valor Final"].sum())
  return {"Faturamento ": faturamento}

@app.route("/vendas/produtos")   # decorator  -  Diz em qual link a função vai rodar
def vendas_produtos():  # função
  tabela_vendas_produtos = tabela[["Produto", "Valor Final"]].groupby("Produto").sum()
  dic_vendas_produtos = tabela_vendas_produtos.to_dict()
  return dic_vendas_produtos

@app.route("/vendas/produtos/<produto>")   # decorator  -  Diz em qual link a função vai rodar
def fat_produto(produto):  # função
  tabela_vendas_produtos = tabela[["Produto", "Valor Final"]].groupby("Produto").sum()
  if produto in tabela_vendas_produtos.index:
    vendas_produto = tabela_vendas_produtos.loc[produto]
    dic_vendas_produto = vendas_produto.to_dict()
    return dic_vendas_produto
  else:
    return {produto: "Inexistente"}
    
  

app.run()    #  no replit use o app.run(host="0.0.0.0")        # coloca o site no ar