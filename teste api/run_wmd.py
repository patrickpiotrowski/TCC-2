def calculate(title, description):
    # Initialize logging.
    import logging

    logging.basicConfig(
        format="%(asctime)s : %(levelname)s : %(message)s", level=logging.INFO
    )

    sentence_obama = "O rato roeu a roupa do Rei de Roma"
    sentence_president = "O camundongo dilascerou as vestes do Senhor Romano"

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
    professores = [
        {
            "nome": "Adriana Herden",
            "email": "herden@utfpr.edu.br",
            "area": "Engenharia de Software, Qualidade de Software, BPMN, BPMS, Robótica Educacional, Gerenciamento Ágil de Projetos",
        },
        {
            "nome": "Adriane Carla Anastácio da Silva",
            "email": "anastacio@utfpr.edu.br",
            "area": "Engenharia de Software, Informática na Educação",
        },
        {
            "nome": "Adriano Rivolli Da Silva",
            "email": "rivolli@utfpr.edu.br",
            "area": "Aprendizado de Máquina, Inteligência Artificial, Meta-aprendizado, Ferramentas jurídicas, Ferramentas para o mercado financeiro de ações, Sistemas de informação interativo e educativos",
        }
    ]

    title_distance_list = []
    description_distance_list = []

    processed_title = preprocess(title)
    processed_description = preprocess(description)

    processed_sentence_obama = preprocess(sentence_obama)
    processed_sentence_president = preprocess(sentence_president)
    ###############################################################################
    # Now, as mentioned earlier, we will be using some downloaded pre-trained
    # embeddings. We load these into a Gensim Word2Vec model class.
    #
    # .. Important::
    #   The embeddings we have chosen here require a lot of memory.
    #

    print(processed_title)

    from gensim.models import Word2Vec, KeyedVectors, Doc2Vec
    from gensim.test.utils import get_tmpfile
    import os

    print(f"{os.getcwd()}/model/w2v.vectors.kv")

    fname = get_tmpfile(f"{os.getcwd()}/./model/w2v.vectors.kv")
    w2v = KeyedVectors.load(fname, mmap="r")

    for word in processed_title:
        print(f"{word}:")
        print("-" * 28)
        for w in w2v.most_similar(word)[:3]:
            print(w[0].ljust(20), round(w[1], 5))
        print()

    ###############################################################################
    # So let's compute WMD using the ``wmdistance`` method.
    #
    contador = 0

    for professor in professores:
        sentence = preprocess(professor['area'])
        print(f"\n sentence: {sentence} \n")
        distance = w2v.wmdistance(processed_title, sentence)
        title_distance_list.append(distance)
        print(f"\n\n distance {contador} = {distance:.4f} \n\n")
        contador = contador + 1

    print(title_distance_list)
    indice_menor_valor = title_distance_list.index(min(title_distance_list))
    print(f"Menor indice: {indice_menor_valor}")
    return professores[indice_menor_valor]

    ###############################################################################
    # Let's try the same thing with two completely unrelated sentences. Notice that the distance is larger.
    #
    # sentence_orange = preprocess("Laranja é minha fruta favorita")
    # distance = w2v.wmdistance(processed_sentence_obama, sentence_orange)

    # print("\n\n distance ruim = %.4f \n\n" % distance)
