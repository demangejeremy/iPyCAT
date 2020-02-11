from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import os
from pathlib import Path

def stopWords(fichier, langue):
    # Recuperer le texte et faire un traitement
    content = open(fichier, "r")
    data = content.read()
    content.close()
    dataWithStop = ""
    stopWords = set(stopwords.words(langue))
    words = word_tokenize(data)
    wordsFiltered = []

    # Imprimer les stop-words
    for w in words:
        if w not in stopWords:
            dataWithStop += w + " "
            wordsFiltered.append(w)

    # Creer un dossier
    path = fichier.rsplit('/', 1)
    path = path[0]
    path = path + "/traitements"
    try:
        os.mkdir(path)
    except OSError:
        print ("Erreur dans la création du dossier : %s" % path)

    # Imprimer le fichier 
    output_path = Path(path + "/stop-words.txt")
    output_path.open("w", encoding="utf-8").write(dataWithStop)

    print("Lien du fichier : " + path + "/stop-words.txt")