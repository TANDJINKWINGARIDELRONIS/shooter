import pygame
from player import player


#creer une classe quit va reprensenter le jeu

class Game :

    def __init__(self) :

        #generer le joueur
        self.player=player()
        self.pressed= {}
        