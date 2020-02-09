#
# iPyCAT - Application en ligne de commande
# @DemangeJeremy - Licence MIT
#

# Importations
import click
import requests
from src.nuage_mots import nuagesMots

# Application principale
@click.group()
def main():
    """
    Interface Python en ligne de commande pour les Analyses Multidimensionnelles de Textes.
    """
    pass

# Nuage de mots
@main.command()
@click.argument('query')
@click.option('--width', default=400, help='Largeur de l\'image générée.')
@click.option('--height', default=200, help='Hauteur de l\'image générée.')
@click.option('--max_words', default=200, help='Nombre de mots maximum dans le nuage.')
@click.option('--background_color', default='white', help='Couleur d\'arrière-fond du nuage')
def nuage_de_mots(query, width, height, max_words, background_color):
    """Générer un nuage de mots."""
    nuagesMots(query, width, height, max_words, background_color)

# Lancement de l'application
if __name__ == "__main__":
    main()