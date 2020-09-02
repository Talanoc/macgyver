# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 09:02:14 2020

@author: 33633
"""


import pygame
# initialisation de pygame
pygame.init()

# création de la fenetre

# size =dimension d'un coté du carré
size=750
x=0
y=0
case=1 
m=0
 
wall_position = []


# création d'une fenetre carré size*size
screen = pygame.display.set_mode(((size),(size)))

# titre de la fenetre
pygame.display.set_caption("Aidez MacGyver à s'échapper !")

# changement d'icone
icon = pygame.image.load('ressource/MacGyver.png')#.convert()
pygame.display.set_icon(icon)

# placer le décor du labyrinthe

#chargement des decors
wall =pygame.image.load('ressource/wall.jpg')#.convert_alpha()
floor =pygame.image.load('ressource/floor.jpg')#.convert_alpha()

#mise en forme des decors

resize_decor= size // 15

wall=pygame.transform.scale(wall,(resize_decor,resize_decor))
floor = pygame.transform.scale(floor,(resize_decor,resize_decor))
   
#remplissage de la fenetre avec l'image floor et creation de la liste numero de case  
    
for n in range (0,size,resize_decor):
    for m in range (0,size,resize_decor):
        wall_position.append([case,n,m])
        case = case + 1 
        screen.blit(floor, (n, m))
      
         # screen.blit(floor, (n, m)) 
          
          
          #screen.blit(wall, (0, 50))
          #screen.blit(wall, (50, 50))
          #screen.blit(wall, (100, 50))
continuer = True            
while continuer:           
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            continuer = False
        pygame.display.flip()
pygame.quit()