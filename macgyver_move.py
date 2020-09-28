# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 11:51:28 2020
@author: 33633
"""
import pygame
from pygame.locals import (K_UP,K_DOWN,K_RIGHT,K_LEFT,K_ESCAPE,KEYDOWN,QUIT,KEYUP)


data_maze=[[0,1,2,3,'floor'],[5,6,7,8,'floor'],[10,11,12,13,'wall'],[15,16,17,18,'wall'],[33,34,35,36,'wall'],
           [0,1,2,3,'floor'],[5,6,7,8,'floor'],[10,11,12,13,'floor'],[15,16,17,18,'floor'],[33,34,35,36,'floor'],
           [0,1,2,3,'floor'],[5,6,7,8,'floor'],[10,11,12,13,'floor'],[15,16,17,18,'floor'],[33,34,35,36,'floor'],
           [0,1,2,3,'floor'],[5,6,7,8,'floor'],[10,11,12,13,'floor'],[15,16,17,18,'floor'],[33,34,35,36,'floor']]
           
pygame.init()
continuer = True            
           
class Macgyver :
       
    def __init__(self,position_macgyver):
        self.position_macgyver=position_macgyver
                                    
    def move_up(self):
        self.move(-15)
        
    def move_down(self):
        self.move(15)
        
    def move_right(self):
        self.move(1)
            
    def move_left(self):
        self.move(-1)
        
          
    def move(self,step_value):
        self.position_macgyver += step_value       
        if data_maze [self.position_macgyver-1][4] == 'floor':
            print('je vais en',self.position_macgyver)
            pass
        else:
            self.position_macgyver -= step_value
            print('je reste en',self.position_macgyver)
        
                  
position_macgyver=16
mac_gyver = Macgyver(position_macgyver)
mac_gyver.move_right()
print (mac.position_macgyver)
mac_gyver.move_up()
print (mac_gyver.position_macgyver)
mac_gyver.move_down()
print (mac_gyver.position_macgyver)
mac_gyver.move_left()
print (mac_gyver.position_macgyver)
mac_gyver.move_right()
print (mac_gyver.position_macgyver)
mac_gyver.move_up()
print (mac_gyver.position_macgyver)
mac_gyver.move_down()
print (mac_gyver.position_macgyver)
mac_gyver.move_left()
print (mac_gyver.position_macgyver)



