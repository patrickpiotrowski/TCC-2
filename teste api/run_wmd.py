def calculate(title, description, id, model):

    contador = 1

    import json
    import os

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
    if contador == 1:
        with open(f"{os.getcwd()}/professors_data/professors.json", 'r', encoding='utf-8') as json_file:
        # Use a função json.load() para carregar o conteúdo do arquivo em uma estrutura de dados Python
            professors = json.load(json_file)
    elif contador == 2:
        with open(f"{os.getcwd()}/professors_data/professors_with_pdf_data.json", 'r', encoding='utf-8') as json_file:
        # Use a função json.load() para carregar o conteúdo do arquivo em uma estrutura de dados Python
            professors = json.load(json_file)
    elif contador == 3:
        with open(f"{os.getcwd()}/professors_data/professors_lattes.json", 'r', encoding='utf-8') as json_file:
        # Use a função json.load() para carregar o conteúdo do arquivo em uma estrutura de dados Python
            professors = json.load(json_file)

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

    with open(f"data/test_{contador}/{id}-{title}-results.json", "a") as arquivo_json:
        json.dump(array, arquivo_json)

    return professors, maxDistances, minDistances, timeTaken

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