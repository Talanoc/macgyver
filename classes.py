# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 10:40:12 2020

@author: 33633
"""
import pygame
from pygame.locals import (K_UP,K_DOWN,K_RIGHT,K_LEFT,K_ESCAPE,KEYDOWN,QUIT,KEYUP)
from constants import (needle,syringe,ether,macgyver,gardien,wall,victoire,rip,maze_name,size,
                       resize_decor,floor,win,old_position,ether_in_bag,needle_in_bag,syringe_in_bag,win)
import pandas
import math
import random

class Maze:
    
    screen=pygame.display.set_mode((size,size))
    
    def __init__(self,maze_name):
        
        self.maze_name = maze_name
 
    
    def load_maze(self):
        
        """
        load maze from xlsx file           
            __entrée:maze_name            
            __traitement interne à la methode : wall_a (sans self puisque inutilisée ailleurs)
            __sortie:self.wall_display (self utilisation en dehors de la methode) contient les numeros appartenant
                au fichier xlsx sans les vides        
        """        
        self.wall_display=[]
        wall_a=[]
        datas = pandas.read_excel ("ressource/labyrinthe.xlsx",self.maze_name)  #datas est un dataframe
        datas = datas.values.tolist()   #datas est une liste de liste
        
        for x in range(15):
            wall_a=wall_a + datas[x]
            self.wall_display = [x for x in wall_a if not math.isnan(x)]        
 
       
    def extract_position_heroes(self): 
        
        """
        create position _macgyver & _guard
        __entree:wall_display
        __x compris entre 226 et 1255 =position_macgyver
        __x superieur à 2000 =position_gardien
        __sortie:self.position_macgyver et self.position_gardien (self utilisation en dehors de la methode)
        
        """        
        for x in self.wall_display:
            if x >225 and x<1255:
                self.position_macgyver =int(x-1000)
            elif x>2000:
                self.position_gardien=int(x-2000)         
   
       
    def maze_generate(self): 
        
        """
        create maze list whit wall an floor [case,n,m,sprite,name]
        __entrée:self.wall_display
        __sortie:self.data_maze au format [case,n,m,sprite,name]
            case :n° de case
            n,m :position des sprites
            sprite:wall ou floor redimensionné
            name:nom de la case ( floor ou wall)
        """         
        case=0
        self.data_maze=[]
                
        #creates the starting data list with all the elements         
        for n in range (0,size,resize_decor):
            for m in range (0,size,resize_decor):
                
                case=case+1
                if case in self.wall_display:
                    self.data_maze.append ([case,n,m,wall,"wall"])            
                else:
                    self.data_maze.append([case,n,m,floor,"floor"]) 
   
                                
    def generate_integrate_items(self): 
               
        """
        generate and integrate the position of the object in the list
        __entrée :list_item interne à la methode
        __generation de 3 nombres aléatoire ayant pour nom 'floor' dans la liste data_maze
        __integration des items dans data_maze
        __integration des heros dans data_maze
        __sortie:self.data_maze (self utilisation en dehors de la methode)
                
        """
        list_item = [needle, "needle", syringe, "syringe" , ether, "ether"]
        y=0
        while y<6:    
            g=random.randint(2,224)    
            if self.data_maze[g-1][4]=='floor':
                self.data_maze[g-1][3]=list_item[y]
                self.data_maze[g-1][4]=list_item[y+1]
                y=y+2             
                   
        #place macgyver et gardien            
        self.data_maze[self.position_macgyver-1][3]=macgyver
        self.data_maze[self.position_macgyver-1][4]="macgyver"
        self.data_maze[self.position_gardien-1][3]=gardien
        self.data_maze[self.position_gardien-1][4]="gardien"
        return self.data_maze
 
       
    def maze_display (self): 
             
        """
        display of the list self.data_maze in the game window
        __entree pygame et self.data_maze
        __sortie :affichage self.data_maze
        """        
        # création d'une fenetre carré size*size
        screen = pygame.display.set_mode(((size),(size)))  
        # titre de la fenetre
        pygame.display.set_caption("Aidez MacGyver à s'échapper !")
        # changement d'icone
        icon = pygame.image.load('ressource/MacGyver.png')#.convert()
        pygame.display.set_icon(icon)
             
        for case,x,y,sprite,name in self.data_maze:
            screen.blit( sprite , ( y , x ))
            
            
    def maze_construct(self):
        
        Maze.load_maze(self)
        Maze.extract_position_heroes(self)
        Maze.maze_generate(self)
        Maze.generate_integrate_items(self)
        Maze.maze_display(self)
        
        
class Macgyver:
    
    screen=pygame.display.set_mode((size,size))
    
    def __init__(self,maze):
       
        self.position_macgyver=maze.position_macgyver
        self.maze=maze
        self.old_position=old_position       
        self.needle_in_bag = needle_in_bag
        self.syringe_in_bag = syringe_in_bag
        self.ether_in_bag = ether_in_bag
        
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
        
        self.old_position=self.position_macgyver
        self.position_macgyver += int(step_value)
        
        if self.maze.data_maze [self.position_macgyver-1][4] == 'wall':             
             self.position_macgyver -= int(step_value)                                    


    def macgyver_move(self):
       
        case1,x1,y1,sprite1,name=self.maze.data_maze[self.old_position-1]
        case,x,y,sprite,name=self.maze.data_maze[self.position_macgyver-1]
        self.screen.blit(wall , ( 700 , 700 ))
        self.screen.blit(floor , ( y1 , x1 ))
        self.screen.blit(macgyver , ( y , x ))
        
        
    def macgyver_win(self):
                       
        if self.maze.data_maze[self.position_macgyver-1][4]== 'gardien' :
            if self.win == True:
                self.screen.blit (victoire , ( 100, 100))
                        
            else:
                self.screen.blit(rip , ( 100, 100))
            
    
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
             
        self.win=self.needle_in_bag & self.syringe_in_bag & self.ether_in_bag   
       
