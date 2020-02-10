from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
 
def stopWords():
    data = "Bonjour à tous, j'espère que vous allez bien !"
    stopWords = set(stopwords.words('french'))
    words = word_tokenize(data)
    wordsFiltered = []

    for w in words:
        if w not in stopWords:
            wordsFiltered.append(w)

    print(wordsFiltered)