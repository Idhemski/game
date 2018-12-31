#import de modules
import module_py as py
import pygame
import time
import sys
import random

pygame.init()



#variables
debut = time.time()
x = 30
y = 30
x_b , y_b = 500 , 500
ver , hor = 0 , 0
valeurs = [-1 , 0 , 1]
changer = 0
touchage = 0      #il faut qu'elle atteigne 3 pour gagner la partie
taille_rectangle = 60
running = True
clock = pygame.time.Clock()
colorations = [py.couleurs["rouge"], py.couleurs["bleu"], py.couleurs["vert"]] 
ind_couleur = 0
changer_couleur = 0
couleur_b = py.couleurs["rouge"]
fin_du_jeu = False
fin = 0

#Police et début d'écriture
myfont = pygame.font.SysFont("papyrus", 40)
texte_fin = pygame.font.SysFont("papyrus", 40)

#fentre principale
taille_fenetre = (1000 , 1000)
fenetre = pygame.display.set_mode(taille_fenetre)


#programme

while running:
    if not fin_du_jeu:
        # Evenements 
        for event in pygame.event.get():
               
            if event.type == pygame.QUIT:
                    running = False
                    fin_du_jeu = True
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                ind_couleur = (ind_couleur + 1)%3
    
        
    
              
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
            
        # Couleur de B
        if changer_couleur == 30:
            couleur_b = random.choice(colorations)
            changer_couleur = 0
    
        changer_couleur += 1    
    
        
        
            
        # Affichage  
        fenetre.fill(py.couleurs["noir"])
        a = pygame.Rect(x,y,taille_rectangle, taille_rectangle)
        b = pygame.Rect(x_b,y_b,taille_rectangle, taille_rectangle)
        pygame.draw.rect(fenetre, colorations[ind_couleur], a)  #celui que l'on bouge
        pygame.draw.rect(fenetre, couleur_b, b)  #celui qu'il faut attraper
        label = myfont.render("You touched it {} times".format(touchage), 1, py.couleurs["blanc"])
        fenetre.blit(label, (150, 30))
        
        
        
        
        # Collision
        if a.colliderect(b) and colorations[ind_couleur] == couleur_b :
            touchage += 1
            
            x , y = 30 , 30
            x_b , y_b = 500 , 500
            
            if touchage == 3:
                fin = time.time()
                fin_du_jeu = True
         
               
        clock.tick(60) # FPS
        pygame.display.flip()
        
    else:
        
        for event in pygame.event.get():
               
            if event.type == pygame.QUIT:
                    running = False
                    fin_du_jeu = True
        
        dure = fin - debut
        fenetre.fill(py.couleurs["noir"])
        label = texte_fin.render("Congratulations, your score {}".format(dure), 1, py.couleurs["blanc"])
        fenetre.blit(label, (150, 30))
        pygame.display.flip()

pygame.quit()
sys.exit()