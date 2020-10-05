# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 11:51:28 2020
@author: 33633
"""
import pygame
from pygame.locals import (K_UP,K_DOWN,K_RIGHT,K_LEFT,K_ESCAPE,KEYDOWN,QUIT,KEYUP)

class Macgyver :
        
    def __init__(self,position_macgyver):
        self.position_macgyver=position_macgyver
                
    def move(self,step_value):
        self.position_macgyver += step_value       
        if data_maze [self.position_macgyver-1][4] == 'floor':
            pass
        else:
            self.position_macgyver -= step_value
                                             
    def move_up(self):
        self.move(-15)
        
    def move_down(self):
        self.move(15)
        
    def move_right(self):
        self.move(1)
            
    def move_left(self):
        self.move(-1)
        
    def key_move(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYUP and event.key==K_UP:
                Macgyver.move_up()
            
            elif event.type == pygame.KEYUP and event.key==K_DOWN:
                Macgyver.move_down()
            
            elif event.type == pygame.KEYUP and event.key==K_RIGHT:
                Macgyver.move_right()
            
            elif event.type == pygame.KEYUP and event.key==K_LEFT:
                Macgyver.move_left()
                 
            elif event.type == pygame.KEYUP and event.key==K_ESCAPE:
                continuer = False
        
           
