import pygame
from projectile import projectile

#creer le joueur (utilisation de sprite qui permet de definir un elements capable de se deplacer)
class player (pygame.sprite.Sprite):
    def __init__(self,game) :
        super().__init__() #initialisation de la super classe sprite
        self.game=game
        self.health= 100
        self.max_health= 100
        self.attack= 20
        self.velocity= 2
        self.all_projectile=pygame.sprite.Group()
        self.image= pygame.image.load('assets/player.png')
        self.rect= self.image.get_rect() #utilisation de rect pour recuperer un rectagle sur l'interface
        self.rect.x= 400
        self.rect.y=500

    #gestion des degats sur le joueur
    def damage(self,amount) :
        if self.health-amount > amount :
            self.health-=amount
        else :
            self.game.game_over()

    #gestion de la barre de sante
    def update_health_bar(self,surface):
        #dessiner la barre de vie
        pygame.draw.rect(surface,(60,63,60),[self.rect.x + 50,self.rect.y +20,self.max_health,5])
        pygame.draw.rect(surface, (111,210,46),[self.rect.x + 50,self.rect.y +20,self.health,5])
  
        
  
  
    
    #gestion du projectile
    def lauch_projectile(self) :
        #creer une instance qui gere le projectile
        self.all_projectile.add(projectile(self))
    #fonctions pour deplacer le joueur vers la gauche ou vers la droite
    def move_right(self) :
        #verifier si le joueur n'est pas en colision avecun monstre
        if not self.game.check_collision(self,self.game.all_monster) :
            self.rect.x += self.velocity

    def move_left(self) :
        self.rect.x -=self.velocity