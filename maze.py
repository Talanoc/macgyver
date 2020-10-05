# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 13:52:28 2020

@author: 33633
"""
import pygame
import pandas
import math
import random
<<<<<<< HEAD
=======
from pygame.locals import (K_UP,K_DOWN,K_RIGHT,K_LEFT,K_ESCAPE,KEYDOWN,QUIT,KEYUP)
from macgyver_move import Macgyver

     
# initialisation de pygame
pygame.init()
>>>>>>> 4d0da99ad9966bfab7d748373d5891ffb68a4a86

size=(750)
nb_case=15
resize_decor=int(size/nb_case)


<<<<<<< HEAD
class Maze:    
    
    def __init__(self,maze_name):
        self.maze_name = maze_name
        pygame.init()
                
    def load_maze(self):
        """load maze from xlsx file"""
        self.wall_display=[]
        self.wall_a=[]
        datas = pandas.read_excel ("ressource/labyrinthe.xlsx",self.maze_name)  #datas est un dataframe
        datas = datas.values.tolist()   #datas est une liste de liste
     
        for x in range(15):
            self.wall_a=self.wall_a + datas[x]
            self.wall_display = [x for x in self.wall_a if not math.isnan(x)]
            
    def extract_position_heroes(self):
         for x in self.wall_display:
            if x >225 and x<1255:
                self.position_macgyver =int(x-1000)
            elif x>2000:
                self.position_gardien=int(x-2000)
                
    def maze_construct(self):
        wall=pygame.transform.scale(pygame.image.load('ressource/wall.png'),(resize_decor,resize_decor))
        floor = pygame.transform.scale(pygame.image.load('ressource/floor.png'),(resize_decor,resize_decor))
        case=0
        self.data_maze=[]
        #creates the starting data list with all the elements         
        for n in range (0,size,resize_decor):
            for m in range (0,size,resize_decor):
                
                case=case+1
                if case in self.wall_display:
                    self.data_maze.append ([case,n,m,wall,"wall"])            
                else:
                    self.data_maze.append([case,n,m,floor,"floor"])                   
             
    def generate_integrate_items(self):
        needle=pygame.transform.scale(pygame.image.load('ressource/aiguille.png'),(resize_decor,resize_decor))
        syringe=pygame.transform.scale(pygame.image.load('ressource/seringue.png'),(resize_decor,resize_decor))
        ether=pygame.transform.scale(pygame.image.load('ressource/ether.png'),(resize_decor,resize_decor))
        macgyver=pygame.transform.scale(pygame.image.load('ressource/MacGyver.png'),(resize_decor,resize_decor))
        gardien=pygame.transform.scale(pygame.image.load('ressource/Gardien.png'),(resize_decor,resize_decor))
                
        list_item = [needle, "needle", syringe, "syringe", ether, "ether"]
        y=0
        while y<6:    
            g=random.randint(2,224)    
            if self.data_maze[g-1][4]=='floor':
                self.data_maze[g-1][3]=list_item[y]
                self.data_maze[g-1][4]=list_item[y+1]
                y=y+2              
                   
        #place macgyver et gardien            
        self.data_maze[self.position_macgyver-1][3]=macgyver
        self.data_maze[self.position_macgyver-1][4]="macgyver"
        self.data_maze[self.position_gardien-1][3]=gardien
        self.data_maze[self.position_gardien-1][4]="gardien"
        return self.data_maze
        
    def maze_display (self):
        
        # création d'une fenetre carré size*size
        screen = pygame.display.set_mode(((size),(size)))  
        # titre de la fenetre
        pygame.display.set_caption("Aidez MacGyver à s'échapper !")
        # changement d'icone
        icon = pygame.image.load('ressource/MacGyver.png')#.convert()
        pygame.display.set_icon(icon)
        
        for case,x,y,sprite,name in self.data_maze:
                screen.blit(sprite , ( y , x ))
         
=======

datas = pandas.read_excel ("C:/Users/33633/desktop/macgyver/ressource/labyrinthe.xlsx","labyrinthe1")  #datas est un dataframe
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

wall =pygame.image.load('ressource/wall.png')#.convert_alpha()
floor =pygame.image.load('ressource/floor.png')#.convert_alpha()
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
        
#debut de la boucle du jeu
"""        
position_macgyver=2
continuer = True 
mac_gyver=Macgyver(position_macgyver)  

         
while continuer:        
           
    for event in pygame.event.get():
    
    # detection of pressing of the up key      
        if event.type == pygame.KEYUP and event.key==K_UP:
            mac_gyver.move_up()
            
    # detection of pressing of the down key                
        elif event.type == pygame.KEYUP and event.key==K_DOWN:
           mac_gyver.move_down()
            
    # detection of pressing of the right key                
        elif event.type == pygame.KEYUP and event.key==K_RIGHT:
            mac_gyver.move_right()
            
    # detection of pressing of the left key               
        elif event.type == pygame.KEYUP and event.key==K_LEFT:
            mac_gyver.move_left()
                
    # detection of pressing of the escape key                
        elif event.type == pygame.KEYUP and event.key==K_ESCAPE:
            continuer = False        
""" 


     
continuer = True            
while continuer:
    
    
    mac_gyver=Macgyver(position_macgyver)
    
    mac_gyver.key_move
    
  
         
    for event in pygame.event.get():
# recording of the last position in the variable pos_precedentx        
        pos_precedent=position_macgyver
# detection of pressing of the up key      
        if event.type == pygame.KEYUP and event.key==K_UP:
            Move.move_up()
            
# detection of pressing of the down key                
        elif event.type == pygame.KEYUP and event.key==K_DOWN:
            Move.move_down()
            
# detection of pressing of the right key                
        elif event.type == pygame.KEYUP and event.key==K_RIGHT:
            Move.move_right()
            
# detection of pressing of the left key               
        elif event.type == pygame.KEYUP and event.key==K_LEFT:
            Move.move_left()
                
# detection of pressing of the escape key                
        elif event.type == pygame.KEYUP and event.key==K_ESCAPE:
            continuer = False
         
for g in position_objets:
        
    number_item=number_item+1
    if g==position_macgyver :
        screen.blit(liste_objets[0] , ( 650 , (number_item*50 )))
# display of the sprite floor at the previous position of macgyver(pos_precedent)          
    
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
>>>>>>> 4d0da99ad9966bfab7d748373d5891ffb68a4a86
