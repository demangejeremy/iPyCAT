from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
 
def stopWords(fichier, langue):
    data = "Bonjour à tous, j'espère que vous allez bien !"
    dataWithStop = ""
    stopWords = set(stopwords.words(langue))
    words = word_tokenize(data)
    wordsFiltered = []

    for w in words:
        if w not in stopWords:
            dataWithStop += w + " "
            wordsFiltered.append(w)

    print(dataWithStop)