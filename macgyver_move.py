# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 11:51:28 2020
@author: 33633
"""

floor_display=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
position_macgyver=17
     
def move_up():
    macgyver_move(-15)    
        
def move_down():
    macgyver_move(15)
    
def move_right():
    macgyver_move(1)
        
def move_left():
    macgyver_move(-1)
           
def macgyver_move(step_value):
    global position_macgyver
    position_macgyver += step_value
    if position_macgyver in floor_display:
        print ("je vais en",position_macgyver)
        return position_macgyver
    else:
        position_macgyver -= step_value
        print ("je reste en",position_macgyver)
        return position_macgyver

# à supprimer quand partie de programme fonctionne  
        
move_up()
move_up()
move_down()
move_right()
move_left()
move_right()
move_up()
move_up()
move_left()
move_down()
move_down()
move_down()
print (position_macgyver)


