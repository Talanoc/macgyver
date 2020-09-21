# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 09:10:32 2020

@author: 33633
"""
import pandas as pd
from pandas import read_excel
import math
import pygame 
import random
size=750
nb_case=15
resize_decor=int(size/nb_case)
case=0
wall_a=[]
data_maze=[]
position_objets=[]
position_macgyver=0 
pygame.init


# chargement des decors 
wall =pygame.image.load('ressource/wall.jpg')
floor =pygame.image.load('ressource/floor.jpg')
needle=pygame.image.load('ressource/aiguille.png')
syringe=pygame.image.load('ressource/seringue.png')
ether=pygame.image.load('ressource/ether.png')
macgyver=pygame.image.load('ressource/MacGyver.png')
gardien=pygame.image.load('ressource/Gardien.png')
victoire=pygame.image.load('ressource/victoire.jpg')
rip=pygame.image.load('ressource/rip.jpg')

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

    

load_sprite()

datas = pd.read_excel ("C:/Users/33633/desktop/macgyver/labyrinthe.xlsx","labyrinthe")  #datas est un dataframe
datas = datas.values.tolist()   #datas est une liste de liste
for x in range(15):
    #x=x-1
    wall_a=wall_a + datas[x]
    wall_display = [x for x in wall_a if not math.isnan(x)]
    
#macgyver and guard position
for x in wall_display:
    if x >225 and x<1255:
        position_macgyver =int(x-1000)
    elif x>2000:
        position_gardien=int(x-2000)
        
#place wall and floor
for n in range (0,size,resize_decor):
    for m in range (0,size,resize_decor):
        
        case=case+1
        if case in wall_display:
            data_maze.append ([case,n,m,wall,"wall"])
            
        else:
            data_maze.append([case,n,m,floor,"floor"])
            
#place macgyver et gardien            
data_maze[position_macgyver-1][3]=macgyver  
data_maze[position_gardien-1][3]=gardien

#position des objets

#position_objets = [needle,"",syringe,"",ether,""] 

x=-1           
while len(position_objets) < 3:
    g=random.randint(2,224)
    print (len(position_objets))
    if g  in wall_display: 
        pass
    else:
        position_objets.append(g)
        
        
position_needle=position_objets[0]
position_ether= position_objets[1]
position_syringe=position_objets[2] 

    
data_maze[position_needle-1][3]=needle
data_maze[position_needle-1][4]="needle"
data_maze[position_ether-1][3]=ether
data_maze[position_ether-1][4]="ether"
data_maze[position_syringe-1][3]=syringe
data_maze[position_syringe-1][4]="syringe"

 
# création d'une fenetre carré size*size
screen = pygame.display.set_mode(((size),(size)))  
# titre de la fenetre
pygame.display.set_caption("Aidez MacGyver à s'échapper !")

# changement d'icone
icon = pygame.image.load('ressource/MacGyver.png')#.convert()
pygame.display.set_icon(icon) 


for case,x,y,sprite,name in data_maze:
    screen.blit(sprite , ( y , x ))
    
pygame.display.flip() 
   
print (data_maze[position_ether-1])

