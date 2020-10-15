# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 10:40:12 2020

@author: 33633
"""
import pygame
from pygame.locals import (K_UP,K_DOWN,K_RIGHT,K_LEFT,K_ESCAPE,KEYDOWN,QUIT,KEYUP)
from constants import (needle,syringe,ether,macgyver,gardien,wall,victoire,rip,maze_name,size,
                       resize_decor,floor)
import pandas
import math
import random

needle_in_bag = False
syringe_in_bag=False
ether_in_bag=False
bag=False
old_position=0

class Macgyver:
    
    screen=pygame.display.set_mode((size,size))
    
    
    def __init__(self,maze):
              
        self.position_macgyver=maze.position_macgyver
        self.maze=maze
        self.old_position=old_position       
        self.needle_in_bag = needle_in_bag
        self.syringe_in_bag = syringe_in_bag
        self.ether_in_bag = ether_in_bag
        
    
    '''
    adds a step according to the press of a key
    
        __entree:position_macgyver et appui d'une touche
        __appel de la fonction move en fixant la step_value
        __sortie:position_macgyver 
    
    '''
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
    
    '''
    check that movement is possible
        __entree:step_value et position_macgyver
        __stockage de la position de départ et calcul la position d'arrivée
        __si le nom de la case est 'wall' le mouvement est impossible
        __soustrait le step_value de la position_macgyver(retour à la position d'origine)
            
    '''
    def move(self,step_value):
        
        self.old_position=self.position_macgyver
        self.position_macgyver += int(step_value)
        
        if self.maze.data_maze [self.position_macgyver-1][4] == 'wall':             
             self.position_macgyver -= int(step_value)                                    

    '''
    assignment of variables according to the old and new position
        __affectation des valeurs concernant old_position
        __affectation des valeurs concernant position macgyver
        __affichage du sprite floor à l'ancienne position
        __affichage du sprite macgyver à la nouvelle position
        __affichage d'un sprite wall pour palier un bug au départ du jeu 
            (old_position=0 au départ du jeu-> index =-1 ->derniere case de la liste)
    
    '''
    def macgyver_move(self):
        
        case1,x1,y1,sprite1,name=self.maze.data_maze[self.old_position-1]
        case,x,y,sprite,name=self.maze.data_maze[self.position_macgyver-1]        
        self.screen.blit(floor , ( y1 , x1 ))
        self.screen.blit(macgyver , ( y , x ))
        self.screen.blit(wall , ( 700 , 700 ))
    '''
    checking if "bag is true" and position_macgyver = position_gardien
        __si le nom de la case est gardien
        __ et si le bag est plein affichage du sprite victoire
        __ sinon affichage du sprite rip

    '''    
    def macgyver_win(self):
                       
        if self.maze.data_maze[self.position_macgyver-1][4]== 'gardien' :
            if self.bag == True:
                self.screen.blit (victoire , ( 100, 100))
                        
            else:
                self.screen.blit(rip , ( 100, 100))
            
    '''
    checking the position of macgyver with respect to objects
        __verifie si le nom de la case est celui d'un objet
        __affecte True quand mac gyver passe sur la case
        __déplace l'objet en bordure
        __si tous les objets sont à True win passe à true (&)
    
    '''
    def item_detect(self): 
                
        if self.maze.data_maze[self.position_macgyver-1][4]== 'ether': 
            
            self.ether_in_bag = True
            self.screen.blit(ether , ( 700, 50 ))
                     
               
        if self.maze.data_maze[self.position_macgyver-1][4]== 'syringe':
            
            self.syringe_in_bag=True
            self.screen.blit(syringe , ( 700, 100 ))
            
            
        if self.maze.data_maze[self.position_macgyver-1][4]== 'needle':
            
            self.needle_in_bag=True
            self.screen.blit(needle , ( 700, 150 ))
             
        self.bag=self.needle_in_bag & self.syringe_in_bag & self.ether_in_bag   
       
