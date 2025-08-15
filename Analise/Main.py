import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import csv


dado = r'C:\Users\allisson.avila\Documents\GitHub\Health-Data-Py\Analise\Mortalidade_Geral_1989.xlsx'

# LOCALIDADE --- btenção de contagem dos locail mais recorrentes de mortalidade

arquivo = pd.read_excel(dado)
contagem = arquivo['LOCALOBITO'].value_counts().reset_index()
contagem.columns = ['Local do Obito', 'Quantidade']

hospital = contagem.loc[contagem['Local do Obito'] == 1, 'Quantidade'].sum()
domicilio = contagem.loc[contagem['Local do Obito'] == 3, 'Quantidade'].sum()
publica = contagem.loc[contagem['Local do Obito'] == 4, 'Quantidade'].sum()
outros = contagem.loc[contagem['Local do Obito'] == 0, 'Quantidade'].sum()

nomes_barras = ["Hospital","Domicilio","outros","Publica"]
valores = [hospital, domicilio,outros, publica]
#plotagem do grafico
plt.figure(figsize = (6,6))
barras = plt.bar(nomes_barras, valores,color='red')
plt.xlabel('Local do Obito')
plt.ylabel('Quantidade')
plt.title('Quantidade de obitos por localidade em 1989')
plt.xticks(contagem['Local do Obito'])
#nomeando as barras
for barra in barras:
    altura = barra.get_height()
    plt.text(barra.get_x() + barra.get_width()/2, altura + 1, str(altura), ha='center', fontsize=8)
plt.show()

generos = arquivo['SEXO'].value_counts().reset_index()
generos.columns = ['SEXO', 'Quantidade']
nulo = generos.loc[generos['SEXO'] == 0, 'Quantidade'].sum()
feminino = generos.loc[generos['SEXO'] == 1, 'Quantidade'].sum()
masculino = generos.loc[generos['SEXO'] == 2, 'Quantidade'].sum()

nomes_generos = ['Masculino','Feminino','Indefinido']
valoresgeneros = [masculino, feminino, nulo]
#plotagem do grafico
plt.figure(figsize = (6,6))
genbarra = plt.bar(nomes_generos, valoresgeneros,color='red')
plt.xlabel('Genero')
plt.ylabel('Quantidade')
plt.title('Quantidade de obitos por genero em 1989')
plt.xticks(contagem['Genero'])
for g in genbarra:
    altura = g.get_height()
    plt.text(g.get) #continua fazendo



