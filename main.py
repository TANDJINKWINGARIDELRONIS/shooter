import pygame 
pygame.init()
from game import Game

#definir une clock
clock=pygame.time.Clock()
FPS=80
#-----------------------------------------Generer la fenetre du jeu---------------------------------- 
pygame.display.set_caption("Shooter")
screen=pygame.display.set_mode((1080,720))

#-----------------------------------------------charger l'image en fond d'ecran-------------------------- 
background=pygame.image.load('assets/bg.jpg')


#importer notre banniere
banner=pygame.image.load('assets/banner.png')
banner=pygame.transform.scale(banner, (500,500))
banner_rect =banner.get_rect()
banner_rect.x= screen.get_width()/4

#charger le bouton pour lancer la partie
play_button=pygame.image.load("assets/button.png")
play_button=pygame.transform.scale(play_button,(400,150))
play_button_rect=play_button.get_rect()
play_button_rect.x=screen.get_width()/3.33
play_button_rect.y=screen.get_height()/2

#----------------------------------------------charger le jeu--------------------------------
game=Game()

#varialble pour garder la fenetre ouverte
running=True 

while running :
    
    #application de l'arriere plan 
    screen.blit(background,(0,-200))

    #verifier si le jeux a commence ou non
    if  game.is_playing :
        #declancher les instruction de la partie
        game.update(screen)
    #verifier si le jeux n'as pa commence
    else :
        #ajouter l'ecran de bienvenue
        screen.blit(play_button,play_button_rect)
        screen.blit(banner,banner_rect)

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
                if game.is_playing :
                    game.player.lauch_projectile()
                else :
                    game.start()
        elif event.type== pygame.KEYUP :
            game.pressed[event.key] =False

        elif event.type == pygame.MOUSEBUTTONDOWN :
            #verifier si la sourris est en colision avec le bouton play
            if play_button_rect.collidepoint(event.pos) :
                #mettre le jeu en mode lance
                game.start()
                #joueur le son 
                game.sound_manager.play('click')
#fixer le nombre de FPS sur ma clock
    clock.tick(FPS)        