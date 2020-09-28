# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 12:46:56 2020

@author: 33633
"""


"""
Created on Fri Sep 18 09:10:32 2020

@author: 33633
"""
import pandas
from pandas import read_excel
import math
import pygame 
import random
size=750
nb_case=15
resize_decor=int(size/nb_case)
maze=''
data_maze=[] 
wall_a=[]
pygame.init
position_macgyver=0
datas=[]

class Maze:   
        
     def __init__(self,maze_name):
        self.maze_name=maze_name
        
                    
     def maze_init(self):
                 
        pygame.init
         
        wall_a=[] 
         
        # load sprite and resize
        wall=pygame.transform.scale(pygame.image.load('ressource/wall.png'),(resize_decor,resize_decor))
        floor = pygame.transform.scale(pygame.image.load('ressource/floor.png'),(resize_decor,resize_decor))
        needle=pygame.transform.scale(pygame.image.load('ressource/aiguille.png'),(resize_decor,resize_decor))
        syringe=pygame.transform.scale(pygame.image.load('ressource/seringue.png'),(resize_decor,resize_decor))
        ether=pygame.transform.scale(pygame.image.load('ressource/ether.png'),(resize_decor,resize_decor))
        macgyver=pygame.transform.scale(pygame.image.load('ressource/MacGyver.png'),(resize_decor,resize_decor))
        gardien=pygame.transform.scale(pygame.image.load('ressource/Gardien.png'),(resize_decor,resize_decor))
        victoire=pygame.transform.scale(pygame.image.load('ressource/victoire.jpg'),(600,600))
        rip=pygame.transform.scale(pygame.image.load('ressource/rip.jpg'),(600,600))
        
        list_item = [needle,"needle",syringe,"syringe",ether,"ether"]
               
        #load xlsx and transform into list without nan
        
        datas = pandas.read_excel ("ressource/labyrinthe.xlsx",maze_name)  #datas est un dataframe
        datas = datas.values.tolist()   #datas est une liste de liste
     
        for x in range(15):
            wall_a=wall_a + datas[x]
            wall_display = [x for x in wall_a if not math.isnan(x)]    
        
        #macgyver and guard position extraction
        #position_gardien=self.position_gardien
        #position_macgyver=self.position_macgyver
        #wall_display=[]
        
        for x in wall_display:
            if x >225 and x<1255:
                position_macgyver =int(x-1000)
            elif x>2000:
                position_gardien=int(x-2000)
          
        case=0
        #creates the starting data list with all the elements         
        for n in range (0,size,resize_decor):
            for m in range (0,size,resize_decor):
                
                case=case+1
                if case in wall_display:
                    data_maze.append ([case,n,m,wall,"wall"])            
                else:
                    data_maze.append([case,n,m,floor,"floor"])
                           
       #generate the item positions and are integrated into the plan            
        y=0
        while y<6:    
            g=random.randint(2,224)    
            if data_maze[g-1][4]=='floor': 
                data_maze[g-1][3]=list_item[y]
                data_maze[g-1][4]=list_item[y+1]
                y=y+2              
                   
        #place macgyver et gardien            
        data_maze[position_macgyver-1][3]=macgyver
        data_maze[position_macgyver-1][4]="macgyver"
        data_maze[position_gardien-1][3]=gardien
        data_maze[position_gardien-1][4]="gardien"
         
         
        # création d'une fenetre carré size*size
        screen = pygame.display.set_mode(((size),(size)))  
        # titre de la fenetre
        pygame.display.set_caption("Aidez MacGyver à s'échapper !")
        # changement d'icone
        icon = pygame.image.load('ressource/MacGyver.png')#.convert()
        pygame.display.set_icon(icon)
        
        print (position_macgyver)
        print (position_gardien)
        
        """
        for case,x,y,sprite,name in data_maze:
                screen.blit(sprite , ( y , x ))
        """       


maze_name='labyrinthe1'
maze_level = Maze(maze_name)
maze_level.maze_init()



"""
pygame.display.flip()
"""


""" 

y=0
while y<6:
    
    g=random.randint(0,8)
    
    if data_maze[g][4]=='floor': 
        data_maze[g][3]=list_item[y]
        data_maze[g][4]=list_item[y+1]
        y=y+2
    
  

#création d'une fenetre carré size*size
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
"""