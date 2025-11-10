import pygame
from player import player
from monster import Mummy
from comet_event import CometFallEvent
from monster import Alien
from son import SoundManager
#creer une classe quit va reprensenter le jeu

class Game :

    def __init__(self) :

        #Definir si le jeu a commence ou non
        self.is_playing=False
        #generer le joueur
        self.all_player=pygame.sprite.Group()
        self.player=player(self)
        #gestion du son
        self.sound_manager=SoundManager()
        self.all_player.add(self.player)
        #Gerer les comettes
        self.comet_event=CometFallEvent(self)
        #definir un groupe de monstre
        self.all_monster= pygame.sprite.Group()
        #definir le score
        self.score=0
        self.font=pygame.font.SysFont("monospace",40) #creation de la police
        self.pressed= {}
     

    def start(self) :
        self.is_playing=True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)
    
    def add_score(self,points) :
        self.score +=points

    def game_over(self) :
        #remettre le jeux a neuf
        self.all_monster=pygame.sprite.Group()
        self.comet_event.all_comets=pygame.sprite.Group()        
        self.player.health=self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing=False
        self.score=0
        #jouer le son 
        self.sound_manager.play('game_over')

    def update(self,screen) :
        #afficher le score en l'ecran
        
        score_text=self.font.render(f"Score : {self.score}",1,(0,0,0))
        screen.blit(score_text,(20,20))
        #appliquer l'image du joueur(blit)
        screen.blit(self.player.image,self.player.rect)

        #actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        
        #actualiser la barre d'evenement du jeu
        self.comet_event.update_bar(screen)

        #Mise a jour de l'animation du joueur
        self.player.update_animation()

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
    

    def spawn_monster(self,monster_class_name) :
        monstre=Mummy(self)
        self.all_monster.add(monster_class_name.__call__(self))
        