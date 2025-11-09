import pygame
from cometes import Comet


#creer une classe pour gerer les evenements de cometes
class CometFallEvent :

    def __init__(self,game) :
        self.percent=0
        self.percent_speed= 10
        self.game=game 
        self.fall_mode=False

        #definir un ensemble de comete
        self.all_comets= pygame.sprite.Group()

    #ajouter un pourcentage a la jauge
    def add_percent(self) :
        self.percent+=self.percent_speed/100

    #detecter si la barre d'evenement est pleine
    def is_full_loaded(self) :
        return self.percent>=100
    
    def reset_percent(self) :
        self.percent=0

    #faire tomber les cometes
    def comet_fall(self) :
        #boucle pour faire apparaitre les cometes
        for i in range (1,10) :
            #faire apparaittre la comette
            self.all_comets.add(Comet(self))

    def attempt_fall(self) :
        #la jauge est totalement chargé
        if self.is_full_loaded() and len(self.game.all_monster)==0:
            self.comet_fall()
            self.fall_mode=True #aciver la pluie de comete
    
    def update_bar(self,surface) :

        #ajouter du pourcentage a la barre
        self.add_percent()

        
        #barre en arriere plan
        pygame.draw.rect(surface,(0,0,0),[
            0, #l'axe des X
            surface.get_height()-20, #l'axe des Y
            surface.get_width(), #la longeur de la barre
            10 #l'epaisseur de la barre
        ])    
        #barre de progression
        pygame.draw.rect(surface,(187,11,11),[
            0, #l'axe des X
            surface.get_height()-20, #l'axe des Y
            (surface.get_width()/100)*self.percent, #la longeur de la barre
            10 #l'epaisseur de la barre
        ])