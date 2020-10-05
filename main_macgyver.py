# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 01:01:23 2020

@author: 33633
"""

import pygame
from pygame.locals import (K_UP,K_DOWN,K_RIGHT,K_LEFT,K_ESCAPE,KEYDOWN,QUIT,KEYUP)
#from macgyver_move import Macgyver
from macgyver_maze import Maze,data_maze



    
pygame.init()
#initialisation du labyrinthe

maze_name=("labyrinthe1")
maze_level = Maze(maze_name)
maze_level.maze_init()


for case,x,y,sprite,name in data_maze:
    if name =='macgyver':
        position_macgyver=case
               
print (position_macgyver) 
for x in data_maze:
    print (data_maze[x])

#print (data_maze [x]) 

"""

continuer = True  
          
#mac_gyver=Macgyver(position_macgyver)    
   
while continuer:        
    for case,x,y,sprite,name in data_maze:
                screen.blit(sprite , ( y , x ))   
    
    print(mac_gyver.position_macgyver)  
           
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
pygame.display.flip()


continuer  
            
"""
       
pygame.quit()   