import pygame 
pygame.init()
from game import Game


#-----------------------------------------Generer la fenetre du jeu---------------------------------- 
pygame.display.set_caption("Shooter")
screen=pygame.display.set_mode((1080,720))

#-----------------------------------------------charger l'image en fond d'ecran-------------------------- 
background=pygame.image.load('assets/bg.jpg')

#----------------------------------------------charger le jeu--------------------------------
game=Game()

#varialble pour garder la fenetre ouverte
running=True 

while running :
    
    #application de l'arriere plan 
    screen.blit(background,(0,-200))

    #appliquer l'image du joueur(blit)
    screen.blit(game.player.image,game.player.rect)

    #recuperer les projectile du joueurs et leur applique le deplacement
    for projectile in game.player.all_projectile :
        projectile.move()

    #appliquer l'ensemble des images du groupes de projectiles
    game.player.all_projectile.draw(screen)
 
    #verifier la direction que l'utilisateur souhaite prendre
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x :
        game.player.move_left()

    #mise a jour de l'ecran
    pygame.display.flip()
    #si le joueur ferme la fenetre
    for event in pygame.event.get() :

    #si l'evenement est fermer la fenetre 
        if event.type==pygame.QUIT :
            running=False
            pygame.quit()

    #si un jour lache une touche du clavier
        elif event.type==pygame.KEYDOWN :
            game.pressed[event.key] =True

            #detecter si la touche espace est active
            if event.key==pygame.K_SPACE :
                game.player.lauch_projectile()
        elif event.type== pygame.KEYUP :
            game.pressed[event.key] =False
        