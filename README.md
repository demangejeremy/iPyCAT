  <h1 align=center>iPyCAT</h1>
  <p align=center>Interface Python en ligne de Commande pour les Analyses de Textes.</p>
<br>

## Préambule

Ces instructions vous permettront d'utiliser au mieux l'application iPyCAT et de l'installer facilement sur votre machine. Nous vous donnons toutes les étapes clés afin de commencer à utiliser notre application rapidement.

### Pré-requis

Afin de lancer l'application iPyCAT sur votre machine, vous devez posséder une version de Python <= 3.7. L'application est multi-plateforme et fonctionne sur Windows, MAC ou Linux.

### Installation

Pour installer iPyCAT sur votre machine, assurez-vous de posséder Python <= 3.7 sur votre machine et dans votre PATH. En ligne de commande, dans votre terminal, installez notre application via PyPI en exécutant la commande suivante :

```
pip install iPyCAT && iPyCAT update
```

Pour mettre à jour l'application iPyCAT, saisir en ligne de commande :

```
pip install --upgrade iPyCAT && iPyCAT update
```

## Prise en main de l'application

Cette section est en cours de développement. De nouveaux exemples seront ajoutés sous peu.

### Générer un nuage de mots

```
iPyCAT nuage-de-mots /chemin/de/mon/document/txt/exemple.txt
```

La liste des paramètres optionnels sont disponibles en saisissant :

```
iPyCAT nuage-de-mots --help
```

### Autres commandes

Saisissez iPyCAT dans votre terminal afin de voir la liste des commandes supportées par notre application.

```
iPyCAT
```

## Questions techniques

En cas de problème pour utiliser iPyCAT, merci de nous contacter par mail afin de résoudre cela ensemble à cette adresse : ipycat@googlegroups.com.

Afin de répondre avec diligence à votre demande, nous vous prions de bien vouloir répondre à ces questions dans votre premier message :

```
> Quelle est votre système d'exploitation ? (Windows, MAC, etc.)
> Quelle est la version du système d'exploitation ? (Windows 10, MACOS 10.15.2, etc.)
> Joignez à votre message la sortie complète affichée en ligne de commandes.
```
