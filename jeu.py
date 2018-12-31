#import de modules
import module_py as py
import    pygame
import      time
import       sys
import random

pygame.init()



#variables
debut            = time.time()
x                = 30
y                = 30

x_b , y_b = 900 , 900
ver , hor = 0 , 0
valeurs = [-1 , 0 , 1]
changer = 0

taille_fenetre   = (1000 , 1000)
taille_rectangle = 60
running          = True
clock = pygame.time.Clock()


#fentre principale
fenetre = pygame.display.set_mode(taille_fenetre)


#programme

while running:
    
    # Evenements 
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
           
    #Mouvement de a
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y >= 0 :
        y -= 2
    if pressed[pygame.K_DOWN] and y + taille_rectangle <= taille_fenetre[1]:
        y += 2
    if pressed[pygame.K_LEFT] and x >= 0:
        x -= 2
    if pressed[pygame.K_RIGHT] and x + taille_rectangle <= taille_fenetre[0] :
        x += 2
        
    
    # Mouvement de B
    if changer == 30:    
        ver , hor = random.choice(valeurs) , random.choice(valeurs)
        changer = 0
    changer += 1    
        
    if x_b + ver*3 >= 0 and x_b + ver*3 + taille_rectangle <= taille_fenetre[0]:
        x_b += ver*3
    
    if y_b + hor*3 >= 0 and y_b + hor*3 + taille_rectangle <= taille_fenetre[1]:
        y_b += hor*3
    
        
    # Affichage  
    fenetre.fill(py.couleurs["noir"])
    a = pygame.Rect(x,y,taille_rectangle, taille_rectangle)
    b = pygame.Rect(x_b,y_b,taille_rectangle, taille_rectangle)
    pygame.draw.rect(fenetre, py.couleurs["bleu"], a)
    pygame.draw.rect(fenetre, py.couleurs["rouge"],b)
    
    # Collision
    if a.colliderect(b):
        running = False
        fin = time.time() 
     
           
    clock.tick(60) # FPS
    pygame.display.flip()

pygame.quit()
sys.exit()