# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 11:51:28 2020
@author: 33633
"""

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
        if position_macgyver in wall_display:
            position_macgyver -= step_value
            return position_macgyver
        else:
            
            
            return position_macgyver




