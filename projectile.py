import pygame 

#defintion de la classe qui gere le projectile du joueur

class projectile (pygame.sprite.Sprite):

    #definir le constructeur de la classe 
    def __init__(self,player) :
        super().__init__()
        self.velocity= 3
        self.player=player
        self.image=pygame.image.load('assets/projectile.png')
        self.image= pygame.transform.scale(self.image,(50,50))
        self.rect= self.image.get_rect()
        self.rect.x=player.rect.x +150
        self.rect.y=player.rect.y +70
        self.origin_image=self.image
        self.angle=0


    #fonction qui fait tourner le projectile
    def rotate(self) :
        self.angle+=12
        self.image=pygame.transform.rotozoom(self.origin_image,self.angle,1)
        self.rect=self.image.get_rect(center=self.rect.center)
    #fonction pour detruire les projectiles
    def remove(self) :
        self.player.all_projectile.remove(self)      
    #definir le deplacement des projectiles a l'ecran
    def move (self) :
        self.rect.x+=self.velocity
        self.rotate()

        #verifier si le projectile entre en colision zvec un monstre
        for monstre in  self.player.game.check_collision(self,self.player.game.all_monster) :
            #supprimer le projectile
            self.remove()
            #infliger des degats
            monstre.damage(self.player.attack)

        #verifier si le projectile n'est plus present sur l'ecran
        if self.rect.x > 900 :
            #supprimer le projectile (en dehors de l'ecran)
            self.remove
    
           