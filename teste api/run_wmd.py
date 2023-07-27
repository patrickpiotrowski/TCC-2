def calculate(title, description, id):
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
            "name": "Adriano Rivolli Da Silva",
            "email": "rivolli@utfpr.edu.br",
            "area": "Aprendizado de Máquina, Inteligência Artificial, Meta-aprendizado, Ferramentas jurídicas, Ferramentas para o mercado financeiro de ações, Sistemas de informação interativo e educativos",
        }
    ]

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
    from gensim.test.utils import get_tmpfile
    import os

    #print(f"{os.getcwd()}/model/w2v.vectors.kv")

    fname = get_tmpfile(f"{os.getcwd()}/model/w2v.vectors.kv")
    w2v = KeyedVectors.load(fname, mmap="r")

    # for word in processed_title:
    #     print(f"{word}:")
    #     print("-" * 28)
    #     for w in w2v.most_similar(word)[:3]:
    #         print(w[0].ljust(20), round(w[1], 5))
    #     print()

    ###############################################################################
    # So let's compute WMD using the ``wmdistance`` method.
    #

    counter = 0
    bigger_distance_title = 0
    min_distance_title = 0
    bigger_distance_desc = 0
    min_distance_desc = 0

    for professor in professors:
        #Preprocessing the area sentence
        processed_area = preprocess(professor["area"])

        # 
        professor["area"] = processed_area

        # calculating distances
        title_distance = w2v.wmdistance(processed_title, processed_area)
        description_distance = w2v.wmdistance(processed_description, processed_area)

        #defining the bigger distances
        if(title_distance > bigger_distance_title):
            bigger_distance_title = title_distance
        if(description_distance > bigger_distance_desc):
            bigger_distance_desc = description_distance
        if(title_distance < min_distance_title):
            min_distance_title = title_distance
        if(description_distance < min_distance_desc):
            min_distance_desc = description_distance

        # adding the distances to the professor object
        professor["title_distance"] = str(round(title_distance, 5))
        professor["description_distance"] = str(round(description_distance, 5))

        print(f"\n\n Title distance {counter} = {title_distance:.4f} \n Desc distance {counter} = {description_distance:.4f}\n")

        # updating the counter
        counter = counter + 1
    # creating fields that hold the max distances
    maxDistances = {
        "title": bigger_distance_title,
        "description": bigger_distance_desc
    }
    minDistances = {
        "title": min_distance_title,
        "description": min_distance_desc
    }

    # returning the data
    return professors, maxDistances, minDistances