import pygame
import random
import animation

#creer la classe qui gere le monstre

class monster (animation.AnimateSprite) :
    def __init__(self,game) :
        super().__init__("mummy")
        self.game=game
        self.health=100
        self.max_health=100
        self.attack=0.3
        self.rect=self.image.get_rect()
        self.rect.x=900 + random.randint(0,300)
        self.rect.y=540
        self.velocity= random.randint(1,3)
    
    #gestion des dommages sur le monstre

    def damage(self,amount) :
        self.health -= amount


        #verifier si la sante est inferieure ou egal a zero
        if self.health <=0 :
            #faire reapparaitre comme un nouveau monstre
            self.rect.x=900 + random.randint(0,300)
            self.health=self.max_health
            self.velocity=random.randint(1,3)

            #si la barre d'evenement est au max
            if self.game.comet_event.is_full_loaded() :
                self.game.all_monster.remove(self)
                #appel de la methode pour essayer la pluie de comete
                self.game.comet_event.attempt_fall()
    
    def update_animation(self) :
        self.animate()
    #gestion de la barre de sante
    def update_health_bar(self,surface):

        #dessiner la barre de vie
        pygame.draw.rect(surface,(60,63,60),[self.rect.x + 10,self.rect.y -20,self.max_health,5])
        pygame.draw.rect(surface, (111,210,46),[self.rect.x + 10,self.rect.y -20,self.health,5])
  

    #fonction qui gere les movement du joueur
    def forward(self) :
        #le deplacement se fait seulement si il y z pas de colision
        if not self.game.check_collision(self,self.game.all_player) :
            self.rect.x-=self.velocity
        #le monstre est en collision  avec le joueur
        else :
            #infligier des degats au joueur
            self.game.player.damage(self.attack)


    