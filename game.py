import pygame
from player import player
from monster import monster
from comet_event import CometFallEvent

#creer une classe quit va reprensenter le jeu

class Game :

    def __init__(self) :

        #Definir si le jeu a commence ou non
        self.is_playing=False
        #generer le joueur
        self.all_player=pygame.sprite.Group()
        self.player=player(self)
        self.all_player.add(self.player)
        #Gerer les comettes
        self.comet_event=CometFallEvent(self)
        #definir un groupe de monstre
        self.all_monster= pygame.sprite.Group()
        self.pressed= {}
     

    def start(self) :
        self.is_playing=True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self) :
        #remettre le jeux a neuf
        self.all_monster=pygame.sprite.Group()
        self.comet_event.all_comets=pygame.sprite.Group()        
        self.player.health=self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing=False

    def update(self,screen) :
        #appliquer l'image du joueur(blit)
        screen.blit(self.player.image,self.player.rect)

        #actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)


        #actualiser la barre d'evenement du jeu
        self.comet_event.update_bar(screen)

        #recuperer les projectile du joueurs et leur applique le deplacement
        for projectile in self.player.all_projectile :
            projectile.move()

        #recuperer les monstres
        for monstre in self.all_monster :
            monstre.forward()
            monstre.update_health_bar(screen)
            monstre.update_animation()
           

        #recuperer les cometes
        for comet in self.comet_event.all_comets :
            comet.fall()
        #appliquer l'ensemble des images du groupes de projectiles
        self.player.all_projectile.draw(screen)
    
        #appliquer l'ensemble des images des groupes de monstres 
        self.all_monster.draw(screen)

        #appliquer les cometes sur l'ecran
        self.comet_event.all_comets.draw(screen)

        #verifier la direction que l'utilisateur souhaite prendre
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x :
            self.player.move_left()
            

    #Gestion des collision
    def check_collision(self,sprite,group) :
        return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)
    

    def spawn_monster(self) :
        monstre=monster(self)
        self.all_monster.add(monstre)
        