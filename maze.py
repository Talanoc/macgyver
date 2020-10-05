# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 13:52:28 2020

@author: 33633
"""
import pygame
import pandas
import math
import random

size=(750)
nb_case=15
resize_decor=int(size/nb_case)


class Maze:    
    
    def __init__(self,maze_name):
        self.maze_name = maze_name
        pygame.init()
                
    def load_maze(self):
        """load maze from xlsx file"""
        self.wall_display=[]
        self.wall_a=[]
        datas = pandas.read_excel ("ressource/labyrinthe.xlsx",self.maze_name)  #datas est un dataframe
        datas = datas.values.tolist()   #datas est une liste de liste
     
        for x in range(15):
            self.wall_a=self.wall_a + datas[x]
            self.wall_display = [x for x in self.wall_a if not math.isnan(x)]
            
    def extract_position_heroes(self):
         for x in self.wall_display:
            if x >225 and x<1255:
                self.position_macgyver =int(x-1000)
            elif x>2000:
                self.position_gardien=int(x-2000)
                
    def maze_construct(self):
        wall=pygame.transform.scale(pygame.image.load('ressource/wall.png'),(resize_decor,resize_decor))
        floor = pygame.transform.scale(pygame.image.load('ressource/floor.png'),(resize_decor,resize_decor))
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
        needle=pygame.transform.scale(pygame.image.load('ressource/aiguille.png'),(resize_decor,resize_decor))
        syringe=pygame.transform.scale(pygame.image.load('ressource/seringue.png'),(resize_decor,resize_decor))
        ether=pygame.transform.scale(pygame.image.load('ressource/ether.png'),(resize_decor,resize_decor))
        macgyver=pygame.transform.scale(pygame.image.load('ressource/MacGyver.png'),(resize_decor,resize_decor))
        gardien=pygame.transform.scale(pygame.image.load('ressource/Gardien.png'),(resize_decor,resize_decor))
                
        list_item = [needle, "needle", syringe, "syringe", ether, "ether"]
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
        
        # création d'une fenetre carré size*size
        screen = pygame.display.set_mode(((size),(size)))  
        # titre de la fenetre
        pygame.display.set_caption("Aidez MacGyver à s'échapper !")
        # changement d'icone
        icon = pygame.image.load('ressource/MacGyver.png')#.convert()
        pygame.display.set_icon(icon)
        
        for case,x,y,sprite,name in self.data_maze:
                screen.blit(sprite , ( y , x ))
         