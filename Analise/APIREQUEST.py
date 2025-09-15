import requests
import pandas as pd

# URL da API do DATASUS
url = "http://apidadosabertos.saude.gov.br/vigilancia-e-meio-ambiente/sistema-de-informacao-sobre-mortalidade"

# Parâmetros da requisição
params = {
    'limit': 1000,
    'offset': 0
}

# Lista para armazenar todos os dados
todos_dados = []

# Exemplo: pegar as primeiras 2 páginas
for i in range(2):
    params['offset'] = i * 1000
    response = requests.get(url, params=params, headers={'accept': 'application/json'})
    if response.status_code == 200:
        df_pag = pd.json_normalize(response.json()['sim'])
        todos_dados.append(df_pag)
        print(f"Página {i+1} carregada")
    else:
        print(f"Erro na página {i+1}: {response.status_code}")

# Concatenar todas as páginas em um único DataFrame
todos_df = pd.concat(todos_dados, ignore_index=True)

# Contagem por código de município
contagem_local = todos_df['codmunres'].value_counts()

# Função para consultar IBGE usando código com 7 dígitos
def obter_nome_municipio_ibge(codigo):
    codigo_str = str(codigo).zfill(7)  # garante 7 dígitos
    url_ibge = f"https://servicodados.ibge.gov.br/api/v1/localidades/municipios/{codigo_str}"
    try:
        r = requests.get(url_ibge)
        if r.status_code == 200:
            return r.json().get('nome')
        else:
            return f"Desconhecido ({codigo})"
    except:
        return f"Desconhecido ({codigo})"

# Mapear todos os códigos para nomes
nomes_municipios = {codigo: obter_nome_municipio_ibge(codigo) for codigo in contagem_local.index}

# Substituir índices da Series pelos nomes
contagem_local.index = contagem_local.index.map(lambda x: nomes_municipios.get(x, f"Desconhecido ({x})"))

# Resultado final
print(contagem_local)
