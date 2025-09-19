
</head>
<body>
  <header>
    <h1>Health-Data-Py</h1>
    <p class="meta">Análise e levantamento de dados sobre óbitos no Brasil (períodos: 1979–1984 e 2017–2022) — foco: feminicídio em Minas Gerais</p>
  </header>

  <section>
    <h2>Resumo</h2>
    <p class="lead">Este documento apresenta a versão acadêmica do projeto <em>Health-Data-Py</em>, cujo objetivo é examinar a influência de fatores sociais, raciais e geográficos sobre os níveis de mortalidade por feminicídio no estado de Minas Gerais. A análise compara dois recortes temporais (1979–1984 e 2017–2022), investigando padrões espaciais e demográficos, diferenças entre sexo e idade, e possíveis associações com o nível de urbanização.</p>
  </section>

  <section>
    <h2>1. Problema de pesquisa</h2>
    <p>Investigar como determinantes sociais e demográficos contribuem para as taxas de mortalidade por feminicídio em Minas Gerais e avaliar a evolução desses indicadores ao longo das últimas décadas. Busca‑se identificar áreas de risco geográfico, disparidades por gênero e idade, bem como possíveis relações com indicadores de urbanização e vulnerabilidade social.</p>
  </section>

  <section>
    <h2>2. Objetivos</h2>
    <h3>2.1 Objetivo geral</h3>
    <p>Quantificar e caracterizar a mortalidade por feminicídio em Minas Gerais, analisando variações temporais e espaciais nas séries históricas selecionadas.</p>
    <h2>2.2 Objetivos específicos</h2>
    <ul>
      <li>Comparar a mortalidade entre sexos e estimar diferenças estatisticamente significativas;</li>
      <li>Identificar municípios e regiões com maior incidência de feminicídio;</li>
      <li>Calcular a idade média de óbito por gênero e por causa;</li>
      <li>Avaliar associações entre nível de urbanização (rural/urbano) e causas de mortalidade;</li>
      <li>Analisar a tendência temporal dos indicadores e possíveis mudanças entre os períodos 1979–1984 e 2017–2022.</li>
    </ul>
  </section>

  <section>
    <h2>3. Perguntas de pesquisa</h2>
    <ol>
      <li>Existe disparidade na mortalidade entre os sexos em Minas Gerais?</li>
      <li>Determinadas regiões ou municípios apresentam taxas mais elevadas de feminicídio?</li>
      <li>Qual é a idade média ao óbito por grupo de gênero?</li>
      <li>Há associação entre nível de urbanização e mortalidade por causas específicas (incluindo feminicídio)?</li>
      <li>Ao longo das décadas avaliadas, os indicadores sociais e demográficos demonstram mudança que possa indicar redução das taxas de mortalidade?</li>
    </ol>
  </section>

  <section>
    <h2>4. Metodologia</h2>
    <p>O fluxo analítico planeado segue etapas reprodutíveis e transparentes:</p>
    <ol>
      <li><strong>Aquisição:</strong> importação dos dados via API governamental (SIM/Sistemas Abertos).</li>
      <li><strong>Pré‑processamento:</strong> seleção e padronização de variáveis relevantes (ano do óbito, causa básica, sexo, idade, raça/cor, código do município de residência, nível de escolaridade e localidade).</li>
      <li><strong>Filtragem temporal:</strong> agrupar o intervalo 1979–1984 em um único bloco para comparação com o período 2017–2022 (análises anuais também serão apresentadas).</li>
      <li><strong>Análises descritivas:</strong> contagens, distribuições por sexo/idade/raça; taxas por 100.000 habitantes quando possível (requer dados populacionais complementares).</li>
      <li><strong>Modelagem exploratória:</strong> testes de hipótese (qui‑quadrado, t‑test) para diferenças entre grupos; análise espacial (mapas de calor, taxas padronizadas por município); séries temporais para detecção de picos.</li>
      <li><strong>Visualização e dashboard:</strong> painéis interativos com gráficos relacionais (histogramas, boxplots, mapas coropléticos, séries temporais).</li>
    </ol>
  </section>

  <section>
    <h2>5. Dados e pré‑processamento</h2>
    <p>Serão realizadas as seguintes operações de tratamento de dados:</p>
    <ul>
      <li>Remoção de registros duplicados e correção de formatos;</li>
      <li>Conversão de códigos para rótulos legíveis (ex.: sexo, raça/cor, naturalidade/município);</li>
      <li>Imputação ou manejo de valores ausentes quando necessário (documentar cada decisão);</li>
      <li>Agrupamento temporal (bloco 1979–1984) e criação de variáveis derivadas (faixa etária, ano, região geográfica).</li>
    </ul>
  </section>

  <section>
    <h2>6. Plano de análises</h2>
    <p>As análises contemplarão, entre outras, as seguintes abordagens:</p>
    <ul>
      <li><strong>Descritiva:</strong> tabelas de frequência, médias, desvios‑padrão e medianas por subgrupos;</li>
      <li><strong>Comparativa:</strong> testes estatísticos para avaliar diferenças por sexo, cor/raça e região;</li>
      <li><strong>Espacial:</strong> mapas coropléticos com taxas por município e análise de clusters (ex.: Anselin Local Moran's I);</li>
      <li><strong>Temporal:</strong> séries temporais e decomposição para identificar tendências e sazonalidade;</li>
      <li><strong>Multivariada:</strong> modelos de regressão (logística ou Poisson) para estimar associações ajustadas entre determinantes sociais e risco de óbito por feminicídio.</li>
    </ul>
  </section>

  <section>
    <h2>7. Resultados esperados</h2>
    <p>Espera‑se identificar padrões geográficos de maior risco, disparidades demográficas (idade, sexo, raça/cor) e possíveis alterações nas taxas entre os períodos comparados. Os resultados serão apresentados com intervalos de confiança e visualizações claras para suporte às interpretações.</p>
  </section>

  <section>
    <h2>8. Conclusão e implicações</h2>
    <p>As conclusões irão sintetizar evidências sobre determinantes sociais e geográficos do feminicídio em Minas Gerais e apontar recomendações para políticas públicas e pesquisas futuras, incluindo limitações dos dados e implicações éticas ao tratar informações sensíveis.</p>
  </section>

  <section>
    <h2>9. Reprodutibilidade</h2>
    <p>Todo o código de extração, limpeza e análise será disponibilizado no repositório <code>Health-Data-Py</code> com um <em>README</em> que documenta dependências, versão de pacotes e instruções para reproduzir os resultados.</p>
  </section>

  <footer>
    <p>Autor: Equipe Health‑Data‑Py &nbsp;|&nbsp; Data: <time datetime="2025-09-19">2025‑09‑19</time></p>
  </footer>
</body>
</html>
