import requests
import pandas as pd

#url da api
url = "http://apidadosabertos.saude.gov.br/vigilancia-e-meio-ambiente/sistema-de-informacao-sobre-mortalidade?limit=20&offset=1"

#parametros da requisição
params = {
    'limit' : 1000,
    'offset' : 1
}

#requisição GET
response = requests.get(url, params=params, headers={'accept': 'application/json'})

#verifica se a conexao deu certo e tenta ja pegar uma planilha de ano especifico
if response.status_code == 200:
    df = pd.DataFrame(response.json()) #transforma em Dataframe do pandas
    df_2020 = df
    print(df_2020.shape)
else:
    print(f"Erro ao consultar dados{response.status_code}")



# PEGANDO TODOS OS DADOS DA API
todos_dados = []
for i in range(0, 4): #vou pegar só 10 paginas como exemplo pra nao sobrecarregar durante o teste
    params = {'limit' : 1000, 'offset' : i}
    r = requests.get(url, params=params, headers={'accept': 'application/json'})
    if r.status_code == 200:
        todos_dados.extend(r.json())
        print(f"todos dados foram para o dataframe {i+1}")
    else:
        print(f"Erro ao consultar dados{r.status_code}")

