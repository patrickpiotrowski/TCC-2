def calculate(title, description, id, model):

    import json

    # Initialize logging.
    import logging

    logging.basicConfig(
        format="%(asctime)s : %(levelname)s : %(message)s", level=logging.INFO
    )

    ###############################################################################
    # These sentences have very similar content, and as such the WMD should be low.
    # Before we compute the WMD, we want to remove stopwords ("the", "to", etc.),
    # as these do not contribute a lot to the information in the sentences.
    #

    # Import and download stopwords from NLTK.
    from nltk.corpus import stopwords
    from nltk import download

    download("stopwords")  # Download stopwords list.
    stop_words = stopwords.words(
        "portuguese"
    )  # there is a stopword list for portuguese

    def preprocess(sentence):
        sentence = sentence.replace(",", " e")
        return [w for w in sentence.lower().split() if w not in stop_words]

    # Define sentences
    professors = [
        {
            "id": 0,
            "name": "Adriana Herden",
            "email": "herden@utfpr.edu.br",
            "area": "Engenharia de Software, Qualidade de Software, BPMN, BPMS, Robótica Educacional, Gerenciamento Ágil de Projetos",
        },
        {
            "id": 1,
            "name": "Adriane Carla Anastácio da Silva",
            "email": "anastacio@utfpr.edu.br",
            "area": "Engenharia de Software, Informática na Educação",
        },
        {
            "id": 2,
            "name": "Adriano Rivolli",
            "email": "rivolli@utfpr.edu.br",
            "area": "Aprendizado de Máquina, Inteligência Artificial, Meta-aprendizado, Ferramentas jurídicas, Ferramentas para o mercado financeiro de ações, Sistemas de informação interativo e educativos",
        },
        {
            "id": 3,
            "name": "Alessandro Silveira Duarte",
            "email": "duarte@utfpr.edu.br",
            "area": "Engenharia de Software",
        },
        {
            "id": 4,
            "name": "Alexandre LErario",
            "email": "alerario@utfpr.edu.br",
            "area": "Desenvolvimento Distribuído, Crowdsourcing, Manutenção de Software, Gestão de Projetos",
        },
        {
            "id": 5,
            "name": "Alexandre Rômolo Moreira Feitosa",
            "email": "alexandrefeitosa@utfpr.edu.br",
            "area": "Desenvolvimento de Software, Programação para Dispositivos Móveis, Informática na Educação, Tutores Inteligentes"
        },
        {
            "id": 6,
            "name": "Alexandre Rossi Paschoal",
            "email": "paschoal@utfpr.edu.br ",
            "area": "Bioinformática, Jogos, Banco de Dados, Aprendizado de Máquina, Desenvolvimento Web, Ferramentas",
        },
        {
            "id": 7,
            "name": "André Luis dos Santos Domingues",
            "email": "anddomingues@utfpr.edu.br",
            "area": "Engenharia de Software",
        },
        {
            "id": 8,
            "name": "André Luiz Przybysz",
            "email": "andrelp@utfpr.edu.br",
            "area": "Desenvolvimento de Software, Desenvolvimento de Novos Produtos, Desenvolvimento Sustentável (ODS), Ferramentas de Tomada de Decisão, Cidades Inteligentes, Engenharia de Software",
        },
        {
            "id": 9,
            "name": "André Yoshiaki Kashiwabara",
            "email": "kashiwabara@utfpr.edu.br",
            "area": "Bioinformática, Reconhecimento de Padrão, Computação Musical, Inteligência Artificial, Teoria da Computação",
        },
        {
            "id": 10,
            "name": "Antonio Carlos Fernandes da Silva",
            "email": "antonio@utfpr.edu.br",
            "area": "Gerenciamento e Projeto de Redes, Arquiteturas de Hardware, Desenvolvimento hardware / Software (arduino, raspberry, UDO, Etc..), Desenvolvimento com FPGAs, Compilação para Hardware",
        },
        {
            "id": 11,
            "name": "Claiton de Oliveira",
            "email": "claitonoliveira@utfpr.edu.br",
            "area": "Visão Computacional, Processamento de Imagens, Computação Gráfica",
        },
        {
            "id": 12,
            "name": "Cléber Gimenez Corrêa",
            "email": "clebergimenez@utfpt.edu.br",
            "area": "Realidade Virtual, Visão Computacional, Teste de Software",
        },
        {
            "id": 13,
            "name": "Danilo Sipoli Sanches",
            "email": "danilosanches@utfpr.edu.br",
            "area": "Inteligência Artificial, Computação Evolutiva, Teoria dos Grafos",
        },
        {
            "id": 14,
            "name": "Debora Goncalves Ribeiro Dias",
            "email": "deboraribeiro@utfpr.edu.br",
            "area": "Tecnologias Assistivas, Ensino de Libras Mediado por Computador",
        },
        {
            "id": 15,
            "name": "Eduardo Cotrin Teixeira",
            "email": "cotrin@utfpr.edu.br",
            "area": "Banco de Dados, e-Science (Big Data), Desenvolvimento de Software , Ferramentas Pedagógicas",
        },
        {
            "id": 16,
            "name": "Eduardo Filgueiras Damasceno",
            "email": "damasceno@utfpr.edu.br",
            "area": "Realidade Virtual, Aumentada, Estendida (RV/RA/XR),  Interfaces Naturais - Natural User Interface Aplicações em Saúde - Informática Médica Neurociência e Neurocomputação - Brain Computer Interface Informática na Educação",
        },
        {
            "id": 17,
            "name": "Érica Ferreira de Souza",
            "email": "ericasouza@utfpr.edu.br",
            "area": "Teste de Software Gestão do Conhecimento na Engenharia de Software",
        },
        {
            "id": 18,
            "name": "Fábio Fernandes da Rocha Vicente",
            "email": "fabiofernandes@utfpr.edu.br",
            "area": "Bioinformática Reconhecimento de Padrões",
        },
        {
            "id": 19,
            "name": "Fabrício Martins Lopes",
            "email": "fabricio@utfpr.edu.br",
            "area": "Bioinformática Reconhecimento de Padrões Inteligência Computacional Processamento de Imagens",
        },
        {
            "id": 20,
            "name": "Flávia Belintani Blum Haddad",
            "email": "flaviahaddad@utfpr.edu.br",
            "area": "Engenharia de software Engenharia de requisitos Processo de software Gestão de Projetos de Software",
        },
        {
            "id": 21,
            "name": "Francisco Pereira Junior",
            "email": "fpereira@utfpr.edu.br",
            "area": "Processamento de Alto Desempenho Programação Paralela e Distribuída Biga Data / Analytics Ciência de Dados Aplicada à Gestão Pública Ciência de Dados Aplicada à Dados Financeiros",
        },
        {
            "id": 22,
            "name": "Gabriel Canhadas Genvigir",
            "email": "gabriel@utfpr.edu.br",
            "area": "Banco de Dados Manutenção de Software Sistemas de Informação",
        },
        {
            "id": 23,
            "name": "Gabriel Costa Silva",
            "email": "gabrielcosta@utfpr.edu.br",
            "area": "Desenvolvimento web Desenvolvimento de aplicações em nuvem/cloudware Evolução arquitetural de software",
        },
        {
            "id": 24,
            "name": "Giovani Volnei Meinerz",
            "email": "giovanimeinerz@utfpr.edu.br",
            "area": "Banco de Dados Gestão de Conhecimento (Big Data)",
        },
        {
            "id": 25,
            "name": "Henrique Yoshikazu Shishido",
            "email": "shishido@utfpr.edu.br",
            "area": "Escalonamento de tarefas Programação para dispositivos móveis Informática em Saúde Computação paralela",
        },
        {
            "id": 26,
            "name": "José Antonio Gonçalves",
            "email": "jgoncalves@utfpr.edu.br",
            "area": "Desenvolvimento de Software Eng. de Software Desenvolvimento Distribuído de Software",
        },
        {
            "id": 27,
            "name": "José Augusto Fabri",
            "email": "fabri@utfpr.edu.br",
            "area": "Engenharia de Software Processo de Software",
        },
        {
            "id": 28,
            "name": "Katia Romero Felizardo Scannavino",
            "email": "katiascannavino@utfpr.edu.br",
            "area": "Engenharia de Software Experimental Revisão Sistemática Mapeamento Sistemático",
        },
        {
            "id": 29,
            "name": "Lucas Dias Hiera Sampaio",
            "email": "ldsampaio@utfpr.edu.br",
            "area": "Segurança em redes de computadores, Sistemas modernos de telecomunicações, Rádio Cognitivo, Blockchain e Aplicações, Otimização e Alocação de Recursos em Telecomunicações",
        },
        {
            "id": 30,
            "name": "Luciano Tadeu Esteves Pansanato",
            "email": "luciano@utfpr.edu.br",
            "area": "Sistemas de Informação Interação Humano-Computador",
        },
        {
            "id": 31,
            "name": "Natássya Barlate Floro da Silva",
            "email": "natassyasilva@utfpr.edu.br",
            "area": "Redes de Computadores Veículos Autônomos Sistemas Embarcados",
        },
        {
            "id": 32,
            "name": "Paulo Augusto Nardi",
            "email": "paulonardi@utfpr.edu.br",
            "area": "Desenvolvimento de Software Jogos Teste de Software Banco de Dados",
        },
        {
            "id": 33,
            "name": "Rodrigo Henrique Cunha Palácios",
            "email": "rodrigopalacios@utfpr.edu.br",
            "area": "IoT Inteligência Artificial Visão Computacional Projetos de Hardware/Software Processamento Digital de Sinais Robótica",
        },
        {
            "id": 34,
            "name": "Rogério Santos Pozza",
            "email": "pozza@utfpr.edu.br",
            "area": "Redes Corporais, Redes de Sensores sem Fio, Redes Ad Hoc, IoT Sistemas Distribuídos Desenvolvimento de Software (arduino, raspberry, web)",
        },
        {
            "id": 35,
            "name": "Rosangela de Fátima Pereira Marquesone",
            "email": "romarquesone@utfpr.edu.br",
            "area": "Big Data / Analytics Ciência de dados Processamento distribuído Tecnologias digitais aplicadas à economia circular",
        },
        {
            "id": 36,
            "name": "Silvio Ricardo Rodrigues Sanches",
            "email": "silviosanches@utfpr.edu.br",
            "area": "Visão Computacional Realidade Aumentada",
        },
        {
            "id": 37,
            "name": "Vanderley Flor da Rosa",
            "email": "vanderley@utfpr.edu.br",
            "area": "Engenharia de Software",
        },
        {
            "id": 38,
            "name": "Willian Massami Watanabe",
            "email": "wwatanabe@utfpr.edu.br",
            "area": "Engenharia de Software Desenvolvimento Web Interação Humano-Computador",
        },
    ]


    import time
    import timeit

    start = timeit.default_timer()

    processed_title = preprocess(title)
    processed_description = preprocess(description)

    ###############################################################################
    # Now, as mentioned earlier, we will be using some downloaded pre-trained
    # embeddings. We load these into a Gensim Word2Vec model class.
    #
    # .. Important::
    #   The embeddings we have chosen here require a lot of memory.
    #

    print(processed_title)
    print(processed_description)

    from gensim.models import Word2Vec, KeyedVectors, Doc2Vec
    import gensim.downloader as api
    from gensim.test.utils import get_tmpfile
    import os

    # print(f"{os.getcwd()}/model/w2v.vectors.kv")

    #fname = get_tmpfile(f"{os.getcwd()}/model/w2v.vectors.kv")
    #w2v = KeyedVectors.load(fname, mmap="r")

    modelUsed = model

    fname = get_tmpfile(f"{os.getcwd()}/model/{modelUsed}.txt")
    w2v = KeyedVectors.load_word2vec_format(fname)
    

    # Google's dataset pre trained model
    # w2v = api.load('word2vec-google-news-300')

    # for word in processed_title:
    #     print(f"{word}:")
    #     print("-" * 28)
    #     for w in w2v.most_similar(word)[:3]:
    #         print(w[0].ljust(20), round(w[1], 5))
    #     print()

    ###############################################################################

    counter = 0
    bigger_distance_title = 0
    min_distance_title = 100
    bigger_distance_desc = 0
    min_distance_desc = 100

    import math 

    for professor in professors:
        # Preprocessing the area sentence
        processed_area = preprocess(professor["area"])

        #
        professor["area"] = processed_area

        # calculating distances
        title_distance = w2v.wmdistance(processed_title, processed_area)
        description_distance = w2v.wmdistance(processed_description, processed_area)

        if( (not math.isinf(title_distance)) or (not math.isinf(description_distance)) ):
            # defining the bigger and minimum distances
            if title_distance > bigger_distance_title:
                bigger_distance_title = title_distance
            elif title_distance < min_distance_title:
                min_distance_title = title_distance

            if description_distance > bigger_distance_desc:
                bigger_distance_desc = description_distance
            elif description_distance < min_distance_desc:
                min_distance_desc = description_distance

            # adding the distances to the professor object
            professor["title_distance"] = str(round(title_distance, 5))
            professor["description_distance"] = str(round(description_distance, 5))

            print(
                f"\n\n Title distance {counter} = {title_distance:.4f} \n Desc distance {counter} = {description_distance:.4f}\n"
            )
        # updating the counter
        counter = counter + 1
    # creating fields that hold the max distances
    maxDistances = {"title": str(bigger_distance_title), "description": str(bigger_distance_desc)}
    minDistances = {"title": str(min_distance_title), "description": str(min_distance_desc)}

    print("Max distances: ")
    print(maxDistances)
    print("Min distances: ")
    print(minDistances)

    finish = timeit.default_timer()

    timeTaken = {
        "timeTaken": finish - start
    }

    array = professors.copy()
    array.insert(0, {
        "id": id,
        "model used": modelUsed,
        "timeTaken": timeTaken["timeTaken"],
        "title": title,
        "description": description,
        "timeTaken": timeTaken,
        "maxDistance": maxDistances,
        "minDistance": minDistances
    })

    print("Time taken: %f seconds" % timeTaken["timeTaken"])

    with open(f"data/{id}-{title}-results.json", "a") as arquivo_json:
        json.dump(array, arquivo_json)

    # return professors, maxDistances, minDistances, timeTaken

    # !!! if testing, use this part and comment the above return !!!!

    def calculate_mean(object):
        title_dist = float(object["title_distance"])
        description_dist = float(object["description_distance"])
        return (title_dist + description_dist) / 2
    for professor in professors:
        del professor["id"]
        del professor["email"]
        del professor["area"]
        professor["media"] = calculate_mean(professor)
    # Ordenar a lista de objetos com base na média das distâncias
    objetos_ordenados = sorted(professors, key=lambda x: x["media"])
    return objetos_ordenados