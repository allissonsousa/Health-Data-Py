import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import csv

dado = r'C:\Users\allisson.avila\Documents\GitHub\Health-Data-Py\PLanilhas\Mortalidade_Geral_1989.xlsx'
#--------------------------------------------------
# LOCALIDADE --- obtenção de contagem dos locais mais recorrentes de mortalidade [hospital,via publica, outros]

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
plt.figure(figsize = (8,8))
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

#-----------------------------------------------
#GENERO --- obtenção da contagem deos óbitos por sexo identificado

Generos = arquivo['SEXO'].value_counts().reset_index()
Generos.columns = ['SEXO', 'Quantidade']

nulo = Generos.loc[Generos['SEXO'] == 0, 'Quantidade'].sum()
feminino = Generos.loc[Generos['SEXO'] == 1, 'Quantidade'].sum()
masculino = Generos.loc[Generos['SEXO'] == 2, 'Quantidade'].sum()

nomes_generos = ['Masculino','Feminino','Indefinido']
valoresgeneros = [masculino, feminino, nulo]

#plotagem do grafico
plt.figure(figsize = (8,8))
genbarra = plt.bar(nomes_generos, valoresgeneros,color='blue')
plt.xlabel('SEXO')
plt.ylabel('Quantidade')
plt.title('Quantidade de obitos por gênero em 1989')
plt.xticks(Generos['SEXO'])
for g in genbarra:
    altura = g.get_height()
    plt.text(g.get_x() + g.get_width()/2, altura + 1, str(altura), ha='center', fontsize=8)

plt.show()

# --------------------------------------------
#IDADE -- análise com base nas idades
# --- Gráfico de Barras (para idades exatas) ---
contaidade = arquivo['IDADE'].value_counts().sort_index()
plt.figure(figsize=(10,10))
plt.bar(contaidade.index, contaidade.values)
plt.xlabel("Idade")
plt.ylabel("Quantidade de pessoas")
plt.title("Recorrência de idades")
plt.show()

# --- Histograma (faixas de idade) ---
plt.figure(figsize=(10,5))
plt.hist(arquivo['IDADE'], bins=10, edgecolor="black")  # bins controla o agrupamento
plt.xlabel("Idade")
plt.ylabel("Frequência")
plt.title("Distribuição de idades")
plt.show()