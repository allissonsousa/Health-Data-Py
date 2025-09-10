import requests
import pandas as pd

#url da api
url = "http://apidadosabertos.saude.gov.br/vigilancia-e-meio-ambiente/sistema-de-informacao-sobre-mortalidade?limit=20&offset=1"

#parametros da requisição
params = {
    'limit' : 1000,
    'offset' : 10
}

#requisição GET
response = requests.get(url, params=params, headers={'accept': 'application/json'})

#verifica se a conexao deu certo e tenta ja pegar uma planilha de ano especifico
if response.status_code == 200:
    df = pd.DataFrame(response.json()) #transforma em Dataframe do pandas
    df_aberto = pd.json_normalize(df['sim'])
    print(df_aberto.head())
    for i, col in enumerate (df.columns):
        print(i, col)
else:
    print(f"Erro ao consultar dados{response.status_code}")



# PEGANDO TODOS OS DADOS DA API
todos_dados = []
for i in range(0, 20): #vou pegar só 20 paginas como exemplo pra nao sobrecarregar durante o teste
    params = {'limit' : 1000, 'offset' : i}
    r = requests.get(url, params=params, headers={'accept': 'application/json'})
    if r.status_code == 200:
        dado_aberto = pd.json_normalize(r.json()['sim'])  #normalizando o json para tabela
        todos_dados.append(dado_aberto)     #adicionando a pagina a lista de paginas
        print(f"Pagina {i+1} carregada com sucesso!")
    else:
        print(f"Erro ao consultar dados{r.status_code}")

todos_df = pd.concat(todos_dados, ignore_index=True)  #unindo todas as paginas em uma só
contagem_sexo = todos_df['sexo'].value_counts()       #contagem dos sexos
print(contagem_sexo)
print("Colunas disponíveis:", todos_df.columns.tolist())



