import requests

link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

requisicao = requests.get(link)
print(requisicao)
print(requisicao.json())


link2 = "https://cep.awesomeapi.com.br/json/94475250"
requisicao2 = requests.get(link2)
print(requisicao2)
print(requisicao2.json())