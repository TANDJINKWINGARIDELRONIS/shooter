import pygame



#definir une classe qui gere les mecaniques d'animation

class AnimateSprite(pygame.sprite.Sprite) :

    #definir les choses a faire a la creation de l'entite
    def __init__(self,name):
        super().__init__()
        self.image=pygame.image.load(f'assets/{name}.png')
        self.current_image=0
        self.images=animations.get(name)
    #definir une methode pour animer le sprite
    
    def animate(self) :
        #passer a l'image suivante 
        self.current_image+=1

        #verifier si ona atteint la fin de l'animation
        if self.current_image>= len(self.images) :
            self.current_image=0

        #modifier l'image de l'anim tion prcedente sur l'animation suivante
        self.image=[self.current_image]    


#definir une fonction qui charge les images d'un sprite

def load_animation_image(sprite_name) :
    #charger les images du sprite dans le dossier correspondant
    images=[]

    #recuperer le chemain du dossier
    path=f"assets/{sprite_name}/{sprite_name}"

    #boucler sur les images
    for num in range(1,24) :
        image_path= path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    #renvoyer le contenu de la liste d'image

    return images 

# dictionaire qui va contenir les images de chaque sprite

animations={
    'mummy' : load_animation_image('mummy')
}