import json
import os
import matplotlib.pyplot as plt
from collections import OrderedDict

yearArray = ['2022', '2023']
modelArray = ['cbow_s50', 'cbow_s100','cbow_s300']

for year in yearArray:
  for model in modelArray:
    with open(f"{os.getcwd()}/test_2_results/{year}_{model}.json", 'r', encoding='utf-8') as json_file:
      # loading the file
      test_result = json.load(json_file, object_pairs_hook=OrderedDict)
      number_result = []
      counter = 0
      # for every work in the file
      for work in test_result:
        # taking the first 5 of the results
        short_results = work["results"][:5]
        for result in short_results:
          if work["orientador"] in result["name"]:
            counter += 1
            object_result = {}
            object_result["titulo_trabalho"] = work["titulo"]
            object_result["orientador"] = work["orientador"]
            object_result["resultado"] = result["name"]
            number_result.append(object_result)

    number_result.insert(0, { 
                                "total": len(test_result),
                                "acertos": counter,
                                "%": round(((counter/len(test_result)) * 100), 2)
                              })
    
    with open(f"number_results/test_2_{year}_{model}.json", "a") as arquivo_json:
      json.dump(number_result, arquivo_json)
      
    print(number_result)