# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:25:33 2020

@author: 33633
"""


# à supprimer quand partie de programme fonctionne
floor_display=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,33]
position_macgyver=17
class Move:

    def __init__(self,position_macgyver,step_value):
        self.position_macgyver=position_macgyver
        self.step_value=step_value
     
    def move_up():
        Move.macgyver_move(-15)    
            
    def move_down():
        Move.macgyver_move(15)
        
    def move_right():
        Move.macgyver_move(1)
            
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

print (position_macgyver)