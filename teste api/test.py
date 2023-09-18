from run_wmd import calculate
import os
import json
import datetime

dataArray = ['2023', '2022']
modelArray = ['cbow_s50', 'cbow_s100','cbow_s300']

for json_data in dataArray:
  with open(f"{os.getcwd()}/pdf_data/{json_data}.json", 'r', encoding='utf-8') as json_file:
    # Use a função json.load() para carregar o conteúdo do arquivo em uma estrutura de dados Python
    data = json.load(json_file)

  resultArray = []

  for model in modelArray:
    for work in data:
      work['results'] = calculate(work['titulo'], work['resumo'], int(datetime.datetime.now().timestamp()), model)
      resultArray.append(work)

    with open(f"test_results/{json_data}_{model}.json", "a") as arquivo_json:
        json.dump(resultArray, arquivo_json)