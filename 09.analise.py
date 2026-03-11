import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

try:
    dados = pd.read_csv('03.BaseDPEvolucaoMensalCisp.csv', sep=';', encoding='iso-8859-1')
    dp = pd.read_csv('08.DP.csv', sep=',', encoding='utf-8')
    df_comDP = dados.merge(dp, left_on='cisp', right_on='codDP', how='left')
    df_sequestro = df_comDP[['cisp', 'nome', 'sequestro', 'regiao', 'ano']]
        
except Exception as e:
    print(f"Erro ao ler o arquivo: {e}")

try: 
    df_sequestro_ano = df_sequestro.groupby('ano')['sequestro'].sum().reset_index()

    df_sequestro_regiao = df_sequestro.groupby('regiao')['sequestro'].sum().reset_index().sort_values(by='sequestro', ascending=False)
except Exception as e:
    print(f"Erro ao processar os dados: {e}")

try:
    plt.subplots(2, 2, figsize=(16, 7))
    plt.suptitle('Análise de Sequestros por Ano e Região', fontsize=16)

    # primeiro gráfico -> por ano (linha)
    plt.subplot(2, 2, 1)
    plt.plot(df_sequestro_ano['ano'], df_sequestro_ano['sequestro'], marker='o', color='green', linewidth=2)  
    plt.xticks(rotation=45)
    
    # segundo gráfico -> por região (barra)
    plt.subplot(2, 2, 2)
    plt.bar(df_sequestro_regiao['regiao'], df_sequestro_regiao['sequestro'])

    # terceiro gráfico -> boxplot
    plt.subplot(2, 2, 3)
    plt.boxplot(df_sequestro['sequestro'], showmeans=True, showfliers=True)

    # quarto quadrante -> boxplot sem outliers
    plt.subplot(2, 2, 4)
    plt.boxplot(df_sequestro['sequestro'], showmeans=True, showfliers=False)
    
    plt.tight_layout()
    plt.show()
except Exception as e:
    print(f"Erro ao criar o gráfico: {e}") 
