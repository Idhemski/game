#import de modules
import pygame
import sys
pygame.init()


#couleurs
noir = (0, 0, 0)
bleu = (0, 0, 255)
rouge = (255, 0, 0)
vert = (0, 255, 0)




#variables 
fin_jeu = False
running = True
valeurs = [-1, 0, 1]
x = y = 30
dio = pygame.time.Clock()



#images
image_a = pygame.image.load('melo.jpg')
image_height = image_a.get_rect().size[1]
image_b = pygame.image.load('cat.jpg')



#fenetre
resolution = (1000, 1000)
fenetre = pygame.display.set_mode(resolution)

#jeu
while running:
    if not fin_jeu:
        
        #evenements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        #bougeages       
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]  and y >= 0 : y -= 2
        if pressed[pygame.K_DOWN] and y + image_height <= resolution[1] : y += 2
        if pressed[pygame.K_LEFT] and x >= 0 : x -= 2
        if pressed[pygame.K_RIGHT] and x + image_height <= resolution[0]  : x += 2
        
        
        #rectage
        mescollisions = [image_b]
        pos_image_a = image_a.get_rect()
        pos_image_b = image_b.get_rect()
        
        #collision
        if pos_image_a.collidelist(pos_image_b) == -1 :
            running = False
        

        #affichage
        fenetre.fill(noir)
        fenetre.blit(image_b, (500, 500))
        fenetre.blit(image_a, (x, y))
        pygame.display.flip()
        dio.tick(60)

#quittage de la fenetre
pygame.quit()
sys.exit()       