import pygame
import random 


#creer une classe qui gere les cometes
class Comet(pygame.sprite.Sprite) :
    def __init__(self,comet_event):
        super().__init__()   
        #defnir l'image de la comete
        self.image= pygame.image.load('assets/comet.png')
        self.rect=self.image.get_rect()
        self.velocity=random.randint(1,3)
        self.rect.x=random.randint(20,800)
        self.rect.y=-random.randint(0,800)
        self.comet_event= comet_event

    def remove(self) :
        self.comet_event.all_comets.remove(self)
        #verifier si le nombre de comete est de zeros
        if len(self.comet_event.all_comets)==0 :
            #remettre la barre a zero
            self.comet_event.reset_percent()
            #remettre les monstre
            self.comet_event.game.spawn_monster()
            self.comet_event.game.spawn_monster()
            self.comet_event.game.spawn_monster()
    #Gerer la chute de la comete
    def fall(self) :
        self.rect.y +=self.velocity

        #verifier si elle ne tombe pas au sol
        if self.rect.y>=500:
        #retirer la comete de l'ecran(Destruction)
            self.remove()
            #verifier s'il y a plus de comete a l'ecran
            if len(self.comet_event.all_comets)==0 :
                #remettre la jauge au depart
                self.comet_event.reset_percent()
                self.comet_event.fall_mode=False

        #verifier si la boule de feu touche le joueur
        if self.comet_event.game.check_collision(
            self, self.comet_event.game.all_player
        ) :
            #suprimer la boule de feu
            self.remove()

            #infliger des degat au joueur
            self.comet_event.game.player.damage(20)
