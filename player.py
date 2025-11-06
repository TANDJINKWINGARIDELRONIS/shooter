import pygame
from projectile import projectile

#creer le joueur (utilisation de sprite qui permet de definir un elements capable de se deplacer)
class player (pygame.sprite.Sprite):
    def __init__(self) :
        super().__init__() #initialisation de la super classe sprite
        self.health= 100
        self.max_health= 100
        self.attack= 10
        self.velocity= 2
        self.all_projectile=pygame.sprite.Group()
        self.image= pygame.image.load('assets/player.png')
        self.rect= self.image.get_rect() #utilisation de rect pour recuperer un rectagle sur l'interface
        self.rect.x= 400
        self.rect.y=500
    
    #gestion du projectile
    def lauch_projectile(self) :
        #creer une instance qui gere le projectile
        self.all_projectile.add(projectile(self))
    #fonctions pour deplacer le joueur vers la gauche ou vers la droite
    def move_right(self) :
        self.rect.x += self.velocity

    def move_left(self) :
        self.rect.x -=self.velocity