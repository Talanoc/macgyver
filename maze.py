# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 00:02:47 2020

@author: 33633
"""


import pygame
import random
from pygame.locals import (K_UP,K_DOWN,K_RIGHT,K_LEFT,K_ESCAPE,KEYDOWN,QUIT,KEYUP)
     
# initialisation de pygame
pygame.init()

# création de la fenetre

# size =dimension d'un coté du carré
size=750
x=0
y=0
case=1
position_macgyver=16
m=0 
pos_precedent=0
wall_position = []

#wall_display =[11,16,17,18,19,21,22,23,24,26,28,29,32,39,41,44,47,49,50,51,52,54,56,57,58,59,62,69,77,79,80,81,82,83,
                #84,85,87,88,89,90,92,94,99,104,107,109,111,112,114,116,117,118,119,122,124,126,129,134,137,139,141,142,
                #143,144,145,146,149,152,154,156,164,167,169,171,173,175,176,177,179,182,184,188,190,199,200,201,202,
                #203,204,205,207,208,209,210,212,220]

wall_display=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,26,30,31,33,34,35,37,38,39,41,43,45,46,50,56,58,60,61,63,
              64,65,67,68,69,70,71,73,75,76,78,80,88,90,91,93,95,97,98,99,100,101,102,103,105,106,108,110,112,
              119,120,121,123,127,129,130,131,132,134,135,136,138,139,140,141,142,144,146,150,151,161,163,165,
              166,167,168,169,170,171,172,173,174,176,178,180,181,184,185,191,193,195,196,197,202,203,204,205,
              206,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225]
floor_display =[]
position_objets=[]
liste=[]
right_wall=[]


#creation d une liste floor
floor_display=list (range(226))
for x in wall_display:
    floor_display.remove(x)   

# création d'une fenetre carré size*size
screen = pygame.display.set_mode(((size),(size)))

# titre de la fenetre
pygame.display.set_caption("Aidez MacGyver à s'échapper !")

# changement d'icone
icon = pygame.image.load('ressource/MacGyver.png')#.convert()
pygame.display.set_icon(icon)

# chargement des décors du labyrinthe

#chargement des decors
wall =pygame.image.load('ressource/wall.jpg').convert_alpha()
floor =pygame.image.load('ressource/floor.jpg').convert_alpha()
needle=pygame.image.load('ressource/aiguille.png')
syringe=pygame.image.load('ressource/seringue.png')
ether=pygame.image.load('ressource/ether.png').convert_alpha()
macgyver=pygame.image.load('ressource/MacGyver.png')
gardien=pygame.image.load('ressource/Gardien.png')

#mise en forme des decors
resize_decor= size // 15

#mise en forme des sprites
gardien=pygame.transform.scale(gardien,(resize_decor,resize_decor))
ether=pygame.transform.scale(ether,(resize_decor,resize_decor))
syringe=pygame.transform.scale(syringe,(resize_decor,resize_decor))
needle=pygame.transform.scale(needle,(resize_decor,resize_decor))
macgyver=pygame.transform.scale(macgyver,(resize_decor,resize_decor))
wall=pygame.transform.scale(wall,(resize_decor,resize_decor))
floor = pygame.transform.scale(floor,(resize_decor,resize_decor))

liste_objets = [needle,syringe,ether] 
 
#remplissage de la fenetre avec l'image floor et creation de la liste numero de case  
    
for n in range (0,size,resize_decor):
    for m in range (0,size,resize_decor):
        wall_position.append([case,n,m])
        case = case + 1 
        screen.blit(floor, (n, m))
      
#placement des murs         
for case_number in wall_display :
    for case,x,y in wall_position :
        if case_number == case :
            screen.blit(wall, ( y , x ))
            
#placement des objets  
            
#generation de nombre aleatoires pour le placement des objets different de la position des murs
            
while len(position_objets) < 3:
    g=random.randint(2,224) 
    for case_number in floor_display:       
        if case_number ==  g :
            position_objets.append(g)   
            
#placement des objets
 

case_number=position_objets[0]
for case,x,y in wall_position :
    if case_number == case :
        screen.blit(ether , ( y , x ))
        
case_number=position_objets[1]
for case,x,y in wall_position :
    if case_number == case :
        screen.blit(needle , ( y , x ))
        
case_number=position_objets[2]
for case,x,y in wall_position :
    if case_number == case :
        screen.blit(syringe , ( y , x ))         
        
screen.blit(macgyver, ( 0 , 50 ))

screen.blit(gardien, ( 700 , 650 ))           
          
        
continuer = True            
while continuer:           
    for event in pygame.event.get():
        pos_precedent=position_macgyver
        
        if event.type == pygame.KEYUP and event.key==K_UP:
            
            position_macgyver=position_macgyver-15
            
            if position_macgyver in floor_display:
                pass
            else:
                position_macgyver=position_macgyver+15
                
        elif event.type == pygame.KEYUP and event.key==K_DOWN:
            
            position_macgyver=position_macgyver+15
           
            if position_macgyver in floor_display:
                pass
            else:
                position_macgyver=position_macgyver-15 
                
        elif event.type == pygame.KEYUP and event.key==K_RIGHT:
            
            position_macgyver=position_macgyver+1
                       
            if position_macgyver in floor_display :
                pass
            else:
                position_macgyver=position_macgyver-1
                
        elif event.type == pygame.KEYUP and event.key==K_LEFT:
            
            position_macgyver=position_macgyver-1            
            
            if position_macgyver in floor_display:
                pass
            else:
                position_macgyver=position_macgyver+1
                
                
                 
        elif event.type == pygame.KEYUP and event.key==K_ESCAPE:
            continuer = False
        
            

        for case,x,y in wall_position:
                if pos_precedent == case :
                    screen.blit(floor , ( y , x ))
        
               
        for case,x,y in wall_position:
                if position_macgyver == case:
                    screen.blit(macgyver , ( y , x )) 
            
         
                                
               # screen.blit(position_macgyver, ( 700 , 700)) 
    pygame.display.flip()
            
pygame.quit()
