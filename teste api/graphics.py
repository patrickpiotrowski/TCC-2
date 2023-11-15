import json
import matplotlib.pyplot as plt
import os
import re

# Função para carregar dados do arquivo JSON
def carregar_dados(opened_file):
    with open(f"{os.getcwd()}/number_results/{opened_file}", 'r') as file:
        return json.load(file)

# Lista de arquivos para cada conjunto de trabalhos
files_2023 = ['test_1_2023_cbow_s50.json', 'test_1_2023_cbow_s100.json', 'test_1_2023_cbow_s300.json']
files_2022 = ['test_1_2022_cbow_s50.json', 'test_1_2022_cbow_s100.json', 'test_1_2022_cbow_s300.json']

# Plotar gráfico com todas as linhas
plt.figure()
plt.title('Desempenho dos Modelos em 2022-2 e 2023-1')

extract_model_info = lambda filename: re.search(r'_([a-zA-Z0-9_]+)\.json', filename).group(1)

# Plotar linhas para cada conjunto de trabalhos
for conjunto, arquivos, cor in zip(['2022-2', '2023-1'], [files_2022, files_2023], ['b', 'g']):
    for arquivo in arquivos:
        dados = carregar_dados(arquivo)
        modelo_info = extract_model_info(arquivo)
        acertos = dados[0]['acertos']
        print(acertos)
        plt.plot(modelo_info, acertos, label=f'{conjunto} - Modelo {modelo_info[0]}', color=cor, linestyle='--')

plt.xlabel('Modelos')
plt.ylabel('Número de Acertos')
plt.legend()
plt.show()