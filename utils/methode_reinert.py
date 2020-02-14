from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import os
from pathlib import Path

# Script methode reinert
def methode_reinert(texte):
    # Variables
    motsStockage = []
    motsTraitements = []
    motsClassification = []
    motsProvisoires = []
    counterProvisoire = []
    motsCount = 0

    # Stockage du fichier
    content = texte.lower()

    # Ajouter les stops words
    stopWords = set(stopwords.words("french"))
    words = word_tokenize(content)

    # Stocker les mots sans stops-words
    for w in words:
        if w not in stopWords:
            motsStockage.append(w)

    # Stockage des mots en unique
    for m in motsStockage:
        if m not in motsTraitements and m not in ['.', ',', '?', '!']:
            motsTraitements.append(m)
            motsCount += 1

    # Ajout en tableau
    for p in motsStockage:
        if p not in ['.', ',', '?', '!']:
            motsProvisoires.append(p)
        else:
            for r in motsTraitements:
                if r in motsProvisoires:
                    counterProvisoire.append(1)
                else:
                    counterProvisoire.append(0)
            motsClassification.append(counterProvisoire)
            motsProvisoires = []
            counterProvisoire = []

    # Generation des graphes
    for g in motsClassification:
        for c in motsClassification:
            if g is not c:
                print(c)
        print('___')

    # Affichage 
    print(motsTraitements)
    print("Mots total :", motsCount)
    # print(motsClassification)

# Appel de la fonction
methode_reinert("""
Le bilan des décès et des contaminations au coronavirus a connu, jeudi 13 février, une forte hausse en Chine après l’adoption par les autorités d’une nouvelle méthode de détection des cas.
Ces nouveaux chiffres pourraient alimenter les spéculations selon lesquelles la gravité de l’épidémie de pneumonie due au nouveau coronavirus, appelée officiellement Covid-19 par l’Organisation mondiale de la santé (OMS), pourrait avoir été sous-estimée. Les ministres européens de la santé doivent se réunir jeudi à Bruxelles pour discuter du sujet.
""")