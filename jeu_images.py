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
image_height_b = image_b.get_rect().size[1]



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
        A = pygame.Rect(x, y, image_height, image_height)
        B = pygame.Rect(500, 500, image_height_b, image_height_b)
        
        #collision
        if A.colliderect(B):
            fin_jeu = True
        
        
        

        #affichage
        fenetre.fill(noir)
        fenetre.blit(image_b, (500, 500))
        fenetre.blit(image_a, (x, y))
        pygame.display.flip()
        dio.tick(60)
   
    else  :
        for event in pygame.event.get():
               
            if event.type == pygame.QUIT:
                    running = False
                    fin_jeu = True

#quittage de la fenetre
pygame.quit()
sys.exit()       