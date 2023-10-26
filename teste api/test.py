# script para rodar automaticamente os testes e gerar os arquivos json

from run_wmd import calculate
import os
import json
import datetime

dataArray = ['2022', '2023']
modelArray = ['cbow_s50', 'cbow_s100','cbow_s300']
# counter = 1

# for json_data in dataArray:
#   with open(f"{os.getcwd()}/pdf_data/{json_data}.json", 'r', encoding='utf-8') as json_file:
#     # Use a função json.load() para carregar o conteúdo do arquivo em uma estrutura de dados Python
#     data = json.load(json_file)


#   for model in modelArray:
#     resultArray = []
#     for work in data:
#       work['results'] = calculate(work['titulo'], work['resumo'], int(datetime.datetime.now().timestamp()), model, counter)
#       resultArray.append(work)

#     with open(f"test_{counter}_results/{json_data}_{model}.json", "a") as arquivo_json:
#         json.dump(resultArray, arquivo_json)

# counter = 2

# for json_data in dataArray:
#   with open(f"{os.getcwd()}/pdf_data/{json_data}.json", 'r', encoding='utf-8') as json_file:
#     # Use a função json.load() para carregar o conteúdo do arquivo em uma estrutura de dados Python
#     data = json.load(json_file)


#   for model in modelArray:
#     resultArray = []
#     for work in data:
#       work['results'] = calculate(work['titulo'], work['resumo'], int(datetime.datetime.now().timestamp()), model, counter)
#       resultArray.append(work)

#     with open(f"test_{counter}_results/{json_data}_{model}.json", "a") as arquivo_json:
#         json.dump(resultArray, arquivo_json)

counter = 3

for json_data in dataArray:
  with open(f"{os.getcwd()}/pdf_data/{json_data}.json", 'r', encoding='utf-8') as json_file:
    # Use a função json.load() para carregar o conteúdo do arquivo em uma estrutura de dados Python
    data = json.load(json_file)


  for model in modelArray:
    resultArray = []
    for work in data:
      work['results'] = calculate(work['titulo'], work['resumo'], int(datetime.datetime.now().timestamp()), model, counter)
      resultArray.append(work)

    with open(f"test_{counter}_results/{json_data}_{model}.json", "a") as arquivo_json:
        json.dump(resultArray, arquivo_json)