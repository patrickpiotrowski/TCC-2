import os
import json

unic_profs = [
  "Adriana Herden",
  "Adriano Rivolli",
  "Alessandro Silveira Duarte",
  "Alexandre Rômolo Moreira Feitosa",
  "Alexandre Rossi Paschoal",
  "André Luiz Przybysz",
  "Antonio Carlos Fernandes da Silva",
  "Claiton de Oliveira",
  "Cléber Gimenez Corrêa",
  "Eduardo Cotrin Teixeira",
  "Eduardo Filgueiras Damasceno",
  "Érica Ferreira de Souza",
  "Fábio Fernandes da Rocha Vicente",
  "Fabrício Martins Lopes",
  "Flávia Belintani Blum Haddad",
  "Francisco Pereira Junior",
  "Gabriel Canhadas Genvigir",
  "Gabriel Costa Silva",
  "Giovani Volnei Meinerz",
  "Henrique Yoshikazu Shishido",
  "José Antonio Gonçalves",
  "Lucas Dias Hiera Sampaio",
  "Natássya Barlate Floro da Silva",
  "Paulo Augusto Nardi",
  "Rodrigo Henrique Cunha Palácios",
  "Rogério Santos Pozza",
  "Rosangela de Fátima Pereira Marquesone",
  "Silvio Ricardo Rodrigues Sanches",
]

dataArray = ['2022', '2023']

contagem_professores = {}

for data in dataArray:  
  with open(f"{os.getcwd()}/number_results/test_3_{data}_cbow_s300.json", 'r', encoding='utf-8') as json_file:
    # Use a função json.load() para carregar o conteúdo do arquivo em uma estrutura de dados Python
    data = json.load(json_file)
    for obj in data:
      orientador = obj.get("orientador")
      
      # Verificar se o orientador está na lista de professores
      if orientador in unic_profs:
        # Incrementar a contagem para esse orientador
        contagem_professores[orientador] = contagem_professores.get(orientador, 0) + 1

contagem_professores_ordenado = dict(sorted(contagem_professores.items()))

# Imprimir a contagem de professores em ordem alfabética
for professor, contagem in contagem_professores_ordenado.items():
    print(f"{professor}: {contagem} vezes")

