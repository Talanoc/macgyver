# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 10:40:11 2020

@author: 33633
"""

import pygame
from pygame.locals import (K_UP,K_DOWN,K_RIGHT,K_LEFT,K_ESCAPE,KEYDOWN,QUIT,KEYUP)
from constants import (maze_name)
from macgyver import Macgyver
from maze import Maze

pygame.init()

def main():
    
    maze=Maze(maze_name)
    maze.maze_construct()
    mac_gyver=Macgyver(maze)
            
    loop = True
            
    while loop:
                    
        for event in pygame.event.get():
                                            
            if event.type == pygame.KEYUP and event.key == K_ESCAPE:
                loop = False
                                                        
            if event.type == pygame.KEYUP:
                
                if event.key == pygame.K_DOWN:                        
                    mac_gyver.move_down()
                if event.key == pygame.K_UP:
                    mac_gyver.move_up()
                if event.key == pygame.K_RIGHT:
                    mac_gyver.move_right()
                if event.key == pygame.K_LEFT:
                    mac_gyver.move_left()
                   
            mac_gyver.macgyver_move()                       
            mac_gyver.item_detect()
            mac_gyver. macgyver_win()
                           
        pygame.display.flip()
        
    pygame.quit()
    
if  __name__ =='__main__':
    main()