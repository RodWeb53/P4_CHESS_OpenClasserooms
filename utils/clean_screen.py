"""Fonctionnalité pour le nettoyage d'écarn Mac et Windows"""
from os import system, name

# Fonction pour le néttoyage de l'écran lors du changement de menu
def clear():
 
    # Pour windows
    if name == 'nt':
        _ = system('cls')
 
    # Pour mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
