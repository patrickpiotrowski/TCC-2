import json
import os
import matplotlib.pyplot as plt
from collections import OrderedDict

yearArray = ['2022', '2023']
modelArray = ['cbow_s50', 'cbow_s100','cbow_s300']

for year in yearArray:
  for model in modelArray:
    with open(f"{os.getcwd()}/test_results/{year}_{model}.json", 'r', encoding='utf-8') as json_file:
      # loading the file
      test_result = json.load(json_file, object_pairs_hook=OrderedDict)
      counter = 0
      # for every work in the file
      for work in test_result:
        # taking the first 5 of the results
        short_results = work["results"][:10]
        for result in short_results:
          if work["orientador"] in result["name"]:
            print(work["orientador"])
            print(result["name"])
            counter += 1
      print(f"acertos {year}_{model}: " + str(counter/len(test_result)))