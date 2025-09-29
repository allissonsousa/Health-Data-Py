import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed
from time import sleep

url = "https://apidadosabertos.saude.gov.br/vigilancia-e-meio-ambiente/sistema-de-informacao-sobre-mortalidade"
limit = 1000
num_paginas = 20  # ajuste conforme necessidade

# Função para buscar uma página
def fetch_page(i):
    params = {'limit': limit, 'offset': i * limit}
    r = requests.get(url, params=params, headers={'accept': 'application/json'})

    if r.status_code == 200:
        try:
            data = r.json().get('sim', [])
            if not data:
                return pd.DataFrame()  # sem dados
            df = pd.json_normalize(data)

            # Filtra apenas colunas existentes com dados
            cols = ['codmunres', 'racacor', 'causabas', 'dtobito']
            cols_existentes = [c for c in cols if c in df.columns]
            df = df[cols_existentes]

            # Remove registros onde todas as colunas estão nulas
            df = df.dropna(how='all', subset=cols_existentes)

            print(f"Página {i+1} retornou {i+i} registros")
            print('---' * 10)

            return df
        except Exception as e:
            print(f"Erro ao processar página {i + 1}: {e}")
            print('=-=' * 10)
            return pd.DataFrame()
    else:
        print(f"Erro ao consultar página {i + 1}: {r.status_code}")
        print('=-=' * 10)
        return pd.DataFrame()


# Usando threads para acelerar
resultados = []
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(fetch_page, i) for i in range(num_paginas)]
    for future in as_completed(futures):
        resultados.append(future.result())

# Concatenando apenas DataFrames válidos
validos = [df for df in resultados if not df.empty]

if validos:
    todos_df = pd.concat(validos, ignore_index=True)
    print("✅ Dados consolidados com sucesso!")
    print('=-=' * 10)
    print("Shape final:", todos_df.shape)
    print('=-=' * 10)
    print("Colunas disponíveis:", todos_df.columns.tolist())
    print('=-=' * 10)
else:
    print("⚠️ Nenhum dado válido retornado da API.")
    print('=⚠️=' * 10)
    todos_df = pd.DataFrame()

# Contagem real sem contar páginas vazias
if not todos_df.empty:
    print(f'Obitos por municipio:\n{todos_df["codmunres"].value_counts(dropna=True)}')
    print('=-=' * 10)
    print(f'Obitos por raça:\n{todos_df["racacor"].value_counts(dropna=True)}')
    print('=-=' * 10)
    print(f'Obitos por causa:\n{todos_df["causabas"].value_counts(dropna=True)}')
    print('=-=' * 10)
    print(f'Obitos por data:\n{todos_df["dtobito"].value_counts(dropna=True)}')
    print('=-=' * 10)
