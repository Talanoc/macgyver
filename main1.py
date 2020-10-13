# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 10:40:11 2020

@author: 33633
"""

import pygame
from pygame.locals import (K_UP,K_DOWN,K_RIGHT,K_LEFT,K_ESCAPE,KEYDOWN,QUIT,KEYUP)
from constants import (needle,syringe,ether,macgyver,gardien,wall,victoire,rip,maze_name,floor,size,win)
from classes import Maze,Macgyver

pygame.init()

maze=Maze(maze_name)
maze.maze_construct()
mac_gyver=Macgyver(maze)
    
loop = True
        
while loop:
    pygame.init()            
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