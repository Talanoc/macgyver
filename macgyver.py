# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 13:52:28 2020

@author: 33633
"""
import pygame
from pygame.locals import (K_UP,K_DOWN,K_RIGHT,K_LEFT,K_ESCAPE,KEYDOWN,QUIT,KEYUP)
from maze import Maze
 

class Macgyver:
    
   
    def __init__(self,position_macgyver):
       
        self.position_macgyver=position_macgyver
        pass
               
                        
    def move_up(self):
       self.move(-15)
       return self.position_macgyver
        
    def move_down(self):
        self.move(15)
        return self.position_macgyver
    def move_right(self):
        self.move(1)
        return self.position_macgyver    
    def move_left(self):
        self.move(-1)                      
        return self.position_macgyver
    
    def move(self,step_value):
        
        self.position_macgyver += int(step_value)
        
        if self.data_maze [self.position_macgyver-1][4] == 'wall':
             
             self.position_macgyver -= int(step_value)                       

    def item_detect(self,win=0):
        
        if self.data_maze[self.position_macgyver-1][4]== 'ether':
            win +=30
            self.screen.blit(self.data_maze[self.position_macgyver-1][3] , ( 700, 50 ))
            
            
        if self.data_maze[self.position_macgyver-1][4]== 'syringe':
            win +=30
            self.screen.blit(self.data_maze[self.position_macgyver-1][3] , ( 700, 100 ))
            
            
        if self.data_maze[self.position_macgyver-1][4]== 'needle':
            win +=40
            self.screen.blit(self.data_maze[self.position_macgyver-1][3] , ( 700, 150 ))
            
            
        if self.data_maze[self.position_macgyver-1][4]== 'gardien' and win == 100 :
            
            self.screen.blit (victoire , ( 100, 100 )) 
        else:
            
            self.screen.blit (rip , ( 100, 100 ))
           
"""       
position_macgyver=16 
mac_gyver=Macgyver(position_macgyver)  

mac_gyver.macgyver_position()     
"""     


       