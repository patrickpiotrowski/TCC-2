from gensim.models import Word2Vec, KeyedVectors, Doc2Vec
from gensim.test.utils import get_tmpfile
import os

# KeyedVectors
fname = get_tmpfile(f"{os.getcwd()}/model/w2v.vectors.kv")
w2v = KeyedVectors.load(fname, mmap='r')

for word in [
    "preto", "branco", "pássaro", "lobo", "mulher", "masculino", "sexo", "montanha", "oceano", 
    "lua", "amor", "senhor", "cimegripe", "nimesulida", "médico",  "doença", "coração", "febre",
    "dor", "coriza", "rancor", "mau", "ódio", "braço", "maçã", "coco", ["lobo", "mau"],
    "espada", "cavaleiro", "rei", "arthur", ["rei", "arthur"]
]:
    print(f"{word}:")
    print("-" * 28)
    for w in w2v.most_similar(word)[:3]:
        print(w[0].ljust(20), round(w[1], 5))
    print()