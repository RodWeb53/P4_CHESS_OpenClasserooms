# ♔ 🏁 - P4_CHESS_OpenClassrooms -  🏁 ♔

## Cette application est dédiée à la gestion des tournois d'échecs.

**Fonctionnalités** 

* La structure du Programme est en '' Model View Controller ''

## Menu principal

    ♔  Menu principal du tournoi d'échec ♔

    ---------------------------------------
    |  1 : Menu joueur
    ---------------------------------------
    |  2 : Menu tournoi
    ---------------------------------------
    |  3 : Menu rapport
    ---------------------------------------
    |  q : Quitter l'application
    --------------------------------------
    
Le menu va permettre la gestion des joueurs, Tournois et rapports 

## Menu Joueur

    ♔ 🏁    Menu gestion des joueurs   🏁 ♔

    ---------------------------------------
    |  1 : Ajouter un joueur
    ---------------------------------------
    |  2 : Menu principal
    ---------------------------------------

- Option 1
    - Création d'un joueur avec les informations suivantes:
        - Nom
        - Prénom
        - Date de naissance

## Menu tournoi

    ♔ 🏁    Menu gestion des tournois   🏁 ♔

    -----------------------------------------
    |  1 : Créer un nouveau tournoi
    -----------------------------------------
    |  2 : Ajouter des joueurs
    -----------------------------------------
    |  3 : Lancer un tournoi
    -----------------------------------------
    |  4 : Terminer un tour
    -----------------------------------------
    |  5 : Lancer un tour
    -----------------------------------------
    |  6 : Commentaire sur le tournoi
    -----------------------------------------
    |  7 : Menu accueil
    -----------------------------------------

- Option 1
    - A la création d'un tournoi il sera demandé:
        - Un nom de tournoi
        - Un emplacement
        - Un nombre de tour (par défaut paramétré à 4)
        - Une date de début de tournoi
- Option 2
    - Ajouter les joueurs que l'on souhaite
        Attention le nombre doit être pair pour lancer le tournoi
- Option 3
    - Permet de lancer le tournoi et de générer le 1° tour de matchs de façon aléatoire
- Option 4
    - Permet la fin d'un tour de match et lors du dernier tour de demander la date de fin de tournoi
- Option 5
    - Permet de relancer un nouveau tour
- Option 6
    - Permet de mettre des commentaires sur le tournoi
    

## Menu Rapport


    ♔ 🏁     Menu gestion des rapports       🏁 ♔ 

    ------------------------------------------------
    |  1 : Liste des joueurs global
    ------------------------------------------------
    |  2 : Liste des tournois
    ------------------------------------------------
    |  3 : Nom et dates d'un tournoi
    ------------------------------------------------
    |  4 : Liste des joueurs d'un tournoi
    ------------------------------------------------
    |  5 : Liste des tours et matchs d'un tournoi
    ------------------------------------------------
    |  6 : Classement d'un tournoi
    ------------------------------------------------
    |  7 : Commentaire d'un tournoi
    ------------------------------------------------
    |  8 : Menu accueil
    ------------------------------------------------

- Option 1
    - permet d'avoir la liste des joueurs de la base de données suivants les classements suivants:
        - Alphabétique
        - Nombre de points
- Option 2
    - Permet d'avoir la liste de tous les tournois de la base de données
- Option 3
    - Permet d'avoir le détail des information d'un tournoi souhaité
- Option 4
    - Permet d'avoir la liste des joueurs pour un tournoi suivants les classements suivants:
        - Alphabétique
        - Nombre de points 
- Option 5
    - Permet d'avoir la liste de tous les matchs par round
- Option 6
    - Permet de voir le classement pour un tournoi
- Option 7
    - Permet de voir les commentaires pour un tournoi souhaité


## Mise en place du programme

`Pré-requis : python 3 doit être installé sur votre machine`

- Télécharger ce code dans ''code'' > ''Download ZIP''
- Décompresser le dossier

### 1. Création de l'environnement virtuel

Ouvrez le terminal, allez dans le dossier que vous avez téléchargé

Tapez la commande suivante pour créer l'environnement virtuel

    python -m venv env

### 2. Lancement de l'environnement virtuel

Sous Windows tapez la commande suivante :

    env\Scripts\activate.bat

Sous MAC ou Linux tapez la commande suivante :

    source env/bin/activate

### 3. Installation des packages

Les packages vont permettre le bon fonctionnement du programme

Tapez la commande suivante pour installer les packages :

    pip install -r requirements.txt

Si vous voulez vérifier que les packages sont bien installés tapez la commande suivante :

    pip freeze


## Lancement du programme

    python main.py

## Générer un rapport avec flake8-html

Le rapport flake8 créer un rapport montrant que le code ne contient pas d'érreur de peluchage

    Le rapport sera créer à l'aide du fichier setup.cfg
    le fichier de configuration permet de ne pas prendre en analyse l'environnement virtuel
    Limite la longueur des lignes à 119
    Et paramètre le répertoire de sortie

    Taper la commende flake8

