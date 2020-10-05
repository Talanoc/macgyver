# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 13:52:29 2020

@author: 33633
"""
import pygame
from pygame.locals import (K_UP,K_DOWN,K_RIGHT,K_LEFT,K_ESCAPE,KEYDOWN,QUIT,KEYUP)
from maze import Maze
from macgyver import Macgyver 

class Game:
    
    def run_game(self):
        
        maze=Maze('labyrinthe1')
        maze.load_maze()
        maze.extract_position_heroes()
        maze.maze_construct()
        maze.generate_integrate_items()        
        maze.maze_display()
        print (maze.data_maze)
        print (maze.position_macgyver)
        print (maze.position_gardien)
        mac_gyver = Macgyver(maze)       
        
        
        continued = True
              
        
        while continued:
            
            for event in pygame.event.get():
                
                
                
                if event.type == pygame.KEYUP and event.key == K_ESCAPE:
                    continued = False
                                        
                if event.type == pygame.KEYUP:
                    
                    if event.key == pygame.K_DOWN:                        
                        mac_gyver.move_down()
                    if event.key == pygame.K_UP:
                        mac_gyver.move_up()
                    if event.key == pygame.K_RIGHT:
                        mac_gyver.move_right()
                    if event.key == pygame.K_LEFT:
                        mac_gyver.move_left()
                
                
                pygame.display.flip()
                
    
game = Game()
game.run_game()
        

    
    
#initialisation du labyrinthe

#initialisation des variables

#placements des items

#debut du jeu

#deplacement de macgyver

#detection de fin de jeu

#fin de jeu
