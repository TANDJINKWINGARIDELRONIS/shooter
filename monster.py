import pygame
import random
import animation

#creer la classe qui gere le monstre

class monster (animation.AnimateSprite) :
    def __init__(self,game,name,size,offset=0) :
        super().__init__(name,size)
        self.game=game
        self.health=100
        self.max_health=100
        self.attack=0.3
        self.rect=self.image.get_rect()
        self.rect.x=900 + random.randint(0,300)
        self.rect.y=540 - offset
        self.loot_amount=10
        self.start_animation()

    def set_speed(self,speed) :
        self.default_speed=speed
        self.velocity= random.randint(1,3)

    def set_loot_amount(self,amount) :
        self.loot_amount=amount

    #gestion des dommages sur le monstre
    def damage(self,amount) :
        self.health -= amount


        #verifier si la sante est inferieure ou egal a zero
        if self.health <=0 :
            #faire reapparaitre comme un nouveau monstre
            self.rect.x=900 + random.randint(0,300)
            self.health=self.max_health
            self.velocity=random.randint(1,self.default_speed)
            #ajouter des point 
            self.game.add_score(self.loot_amount)
            #si la barre d'evenement est au max
            if self.game.comet_event.is_full_loaded() :
                self.game.all_monster.remove(self)
                #appel de la methode pour essayer la pluie de comete
                self.game.comet_event.attempt_fall()
    
    def update_animation(self) :
        self.animate(loop=True)
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

#definir une classe pour la momie
class Mummy(monster) :
    def __init__(self, game):
        super().__init__(game,"mummy",(130,130))
        self.set_speed(3)
        self.set_loot_amount(20)
#definir une classe pour l'alien
class Alien(monster) :
    def __init__(self,game) :
        super().__init__(game,"alien",(300,300),120) 
        self.health=250
        self.max_health=250
        self.attack=0.8
        self.set_speed(1)
        self.set_loot_amount(50)

    