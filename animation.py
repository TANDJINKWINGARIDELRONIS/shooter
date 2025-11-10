import pygame



#definir une classe qui gere les mecaniques d'animation

class AnimateSprite(pygame.sprite.Sprite) :

    #definir les choses a faire a la creation de l'entite
    def __init__(self,name,size=(200,200)):
        super().__init__()
        self.size=size
        self.image=pygame.image.load(f'assets/{name}.png')
        self.image=pygame.transform.scale(self.image,size)
        self.current_image=0
        self.images=animations.get(name)
        self.animation=False

    #definir une methode pour lancer l'animation
    def start_animation(self) :
        self.animation=True   
    #definir une methode pour animer le sprite
    def animate(self,loop=False) :
        if self.animation : #verifie si il y a animation 
            #passer a l'image suivante 
            self.current_image+=1

            #verifier si ona atteint la fin de l'animation
            if self.current_image>= len(self.images) :
                self.current_image=0
                #verifier si l'anomation n'est pas en mode boucle
                if loop is False :
                    #desactiver l'animation
                    self.animation=False

            #modifier l'image de l'anim tion prcedente sur l'animation suivante
            self.image=self.images[self.current_image]    
            self.image=pygame.transform.scale(self.image,self.size)

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
    'mummy' : load_animation_image('mummy'),
    'player' : load_animation_image('player'),
    'alien' : load_animation_image('alien')
}