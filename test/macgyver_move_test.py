# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:25:33 2020

@author: 33633
"""
import pygame
from pygame.locals import (K_UP,K_DOWN,K_RIGHT,K_LEFT,K_ESCAPE,KEYDOWN,QUIT,KEYUP)

<<<<<<< HEAD:test/macgyver_move_test.py

# à supprimer quand partie de programme fonctionne
floor_display=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,33]
position_macgyver=17
class Move:
=======
>>>>>>> 4d0da99ad9966bfab7d748373d5891ffb68a4a86:macgyver_move.py

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
            
<<<<<<< HEAD:test/macgyver_move_test.py
    def move_left():
        Move.macgyver_move(-1)
               
    def macgyver_move(step_value):
        global position_macgyver
        position_macgyver += step_value
        if position_macgyver in floor_display:
            position_macgyver -= step_value
            print ("je reste en",position_macgyver)
            return position_macgyver
        else:
            print ("je vais en",position_macgyver)
            return position_macgyver

# à supprimer quand partie de programme fonctionne  
        
Move.move_up()
Move.move_up()
Move.move_down()
Move.move_right()
Move.move_left()
Move.move_right()
Move.move_up()
Move.move_up()
Move.move_left()
Move.move_down()
Move.move_down()
Move.move_down()
Move.move_left()
Move.move_left()
Move.move_down()
=======
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
>>>>>>> 4d0da99ad9966bfab7d748373d5891ffb68a4a86:macgyver_move.py

print (position_macgyver)