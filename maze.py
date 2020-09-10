# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 12:30:53 2020

@author: 33633
"""


# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 00:02:47 2020

@author: 33633
"""
import math
from math import isnan
import pandas
from pandas import read_excel
import pygame
import random
from pygame.locals import (K_UP,K_DOWN,K_RIGHT,K_LEFT,K_ESCAPE,KEYDOWN,QUIT,KEYUP)
     
# initialisation de pygame
pygame.init()

# création de la fenetre

#variables
size = 750 # windows size
case = 1
number_item = 0
#fin = 3
wall_a=[]
wall_position = []
fichier_read=[]
floor_display=[]
liste_objets=[]
wall_display=[]
position_objets=[]
final=[]
df=[]


datas = pandas.read_excel ("C:/Users/33633/desktop/macgyver/labyrinthe.xlsx","labyrinthe2")  #datas est un dataframe
datas = datas.values.tolist()   #datas est une liste
for x in range(15):
    x=x-1
    wall_a=wall_a + datas[x]
    wall_display = [x for x in wall_a if not math.isnan(x)]
    
       
for x in wall_display:
    if x<2000 and x>1000:
        position_macgyver=(x-1000)    
        wall_display.remove (x)
    elif x>2000 :
       position_gardien=(x-2000)
       wall_display.remove (x)
# macgyver & gardien position
#position_macgyver=16
#position_gardien=210


# creation d une liste floor
floor_display=list(range(226))
for pos in wall_display:
    floor_display.remove (pos)  

# création d'une fenetre carré size*size
screen = pygame.display.set_mode(((size),(size)))

# titre de la fenetre
pygame.display.set_caption("Aidez MacGyver à s'échapper !")

# changement d'icone
icon = pygame.image.load('ressource/MacGyver.png')#.convert()
pygame.display.set_icon(icon)

# chargement des décors du labyrinthe

# chargement des decors

wall =pygame.image.load('ressource/wall.jpg')#.convert_alpha()
floor =pygame.image.load('ressource/floor.jpg')#.convert_alpha()
needle=pygame.image.load('ressource/aiguille.png')
syringe=pygame.image.load('ressource/seringue.png')
ether=pygame.image.load('ressource/ether.png')#.convert_alpha()
macgyver=pygame.image.load('ressource/MacGyver.png')
gardien=pygame.image.load('ressource/Gardien.png')
victoire=pygame.image.load('ressource/victoire.jpg')
rip=pygame.image.load('ressource/rip.jpg')

resize_decor= size // 15

# mise en forme des sprites

gardien=pygame.transform.scale(gardien,(resize_decor,resize_decor))
ether=pygame.transform.scale(ether,(resize_decor,resize_decor))
syringe=pygame.transform.scale(syringe,(resize_decor,resize_decor))
needle=pygame.transform.scale(needle,(resize_decor,resize_decor))
macgyver=pygame.transform.scale(macgyver,(resize_decor,resize_decor))
wall=pygame.transform.scale(wall,(resize_decor,resize_decor))
floor = pygame.transform.scale(floor,(resize_decor,resize_decor))
victoire=pygame.transform.scale(victoire,(600,600))
rip=pygame.transform.scale(rip,(600,600))


liste_objets = [needle,syringe,ether] 
 
# fill the window with the floor image and create the box number list 
    
for n in range (0,size,resize_decor):
    for m in range (0,size,resize_decor):
        wall_position.append([case,n,m])
        case = case + 1 
        screen.blit(floor, (n, m))
      
# placement des murs 
        
for case_number in wall_display :
    for case,x,y in wall_position :
        if case_number == case :
            screen.blit(wall, ( y , x ))
            
# generation of random numbers for the placement of objects different from the position of the walls
            
while len(position_objets) < 3:
    g=random.randint(2,224) 
    for case_number in floor_display:       
        if case_number ==  g :
            position_objets.append(g)   
            
# placement of objects
 
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

for case,x,y in wall_position:
    if case == position_macgyver:
        screen.blit(macgyver, ( y , x ))  
        
for case,x,y in wall_position:
    if case == position_gardien:
        screen.blit(gardien, ( y , x ))
        
continuer = True            
while continuer:           
    for event in pygame.event.get():
# recording of the last position in the variable pos_precedentx        
        pos_precedent=position_macgyver
# detection of pressing of the up key      
        if event.type == pygame.KEYUP and event.key==K_UP:
            
            position_macgyver=position_macgyver-15
            
            if position_macgyver in floor_display:
                pass
            else:
                position_macgyver=position_macgyver+15
# detection of pressing of the down key                
        elif event.type == pygame.KEYUP and event.key==K_DOWN:
            
            position_macgyver=position_macgyver+15
           
            if position_macgyver in floor_display:
                pass
            else:
                position_macgyver=position_macgyver-15 
# detection of pressing of the right key                
        elif event.type == pygame.KEYUP and event.key==K_RIGHT:
            
            position_macgyver=position_macgyver+1
                       
            if position_macgyver in floor_display :
                pass
            else:
                position_macgyver=position_macgyver-1
# detection of pressing of the left key               
        elif event.type == pygame.KEYUP and event.key==K_LEFT:
            
            position_macgyver=position_macgyver-1            
            
            if position_macgyver in floor_display:
                pass
            else:
                position_macgyver=position_macgyver+1
                
# detection of pressing of the escape key                
        elif event.type == pygame.KEYUP and event.key==K_ESCAPE:
            continuer = False
            
        for g in position_objets:
            
            number_item=number_item+1
            if g==position_macgyver :
                screen.blit(liste_objets[0] , ( 650 , (number_item*50 )))
# display of the sprite floor at the previous position of macgyver(pos_precedent)          

        for case,x,y in wall_position:
            if pos_precedent == case :
                screen.blit(floor , ( y , x ))
        
# display of the sprite macgyver at position_macgyver              
        for case,x,y in wall_position:
                if position_macgyver == case:
                    screen.blit(macgyver , ( y , x )) 
        
        if position_macgyver==position_objets[0]:
            final.append(position_macgyver)
            screen.blit(ether , ( 700, 50 ))
            
        elif position_macgyver==position_objets[1]:
            final.append(position_macgyver)
            screen.blit(needle , ( 700,100 ))
                        
        elif position_macgyver==position_objets[2]:
            final.append(position_macgyver)
            screen.blit(syringe , ( 700, 150 ))
        else:
            pass

        if position_macgyver==position_gardien:
            
            final = list(set(final))
            if len(final)==3 :
                screen.blit(victoire , ( 100, 100 )) 
            else:
                screen.blit(rip , ( 100, 100 ))  
            continuer  
                
        pygame.display.flip()
       
pygame.quit()