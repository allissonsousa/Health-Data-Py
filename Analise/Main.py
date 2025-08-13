"""Link para acessar os dados https://dados.gov.br/dados/conjuntos-dados/sim-1979-2019>> """

import csv
import os

"""Rascunho da analise"""

"""
Levantamento da problematica?
O que vai ser analisado?
Qual a relevância dos dados?
Levantamento da solução viável baseada nos dados !
Amostragem de dados !
Analise qualitativa por uso de chatbot !

"""

"""
==Problemática sugerida:

 - Quais desigualdades sociais e 
regionais influenciam as taxas de mortalidade por causas evitáveis no Brasil?
- Alem disso ao longo dos anos como esses dados têm se comportado levantando principais causas para flutuação dos dados


== Por que essa problemática é relevante :

- Causas evitáveis (ex.: doenças prevenidas por vacinação, condições tratáveis com atendimento médico básico, violência) 
são indicadores diretos da qualidade de vida e do acesso a serviços públicos.
- Comparar raça/cor e região de origem pode revelar desigualdades históricas e estruturais.
- A idade pode mostrar impactos diferenciados entre faixas etárias (crianças, jovens, idosos).
- O cruzamento desses dados ajuda a identificar populações mais vulneráveis e políticas públicas prioritárias.


== Há disparidade na mortalidade por causas evitáveis entre diferentes raças/cores no Brasil?

- Certas regiões apresentam mortalidade evitável maior, mesmo com perfis demográficos semelhantes?
- Qual é a idade média de óbito para cada grupo racial ou regional em causas específicas?
- Existe associação entre nível de urbanização da origem e mortalidade por determinadas causas?
- As principais causas de morte evitáveis variam significativamente entre grupos demográficos?
"""

"""
FLUXO DO CODIGO

1 - filtrar dados relevantes e dados que não são relevantes, transformando os arquivos csv e eliminando colunas que nao sao do meu interesse
2 - levantar oque são causas evitáveis de obito
3 - fazer uma relação raça x região x causas evitáveis
4 - fazer o mesmo para os outros anos
5 - imprimir isso através de dashboards personalizáveis e que imprimam gráficos relacionais
6 - fazer a relação entre todos os anos, levantando picos, possíveis causas de aumento/queda
7 - visão geral do comportamento dos dados ao longo dos anos
8 - conclusão da analise qualitativa por modelo de IA"""