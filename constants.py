# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 10:40:13 2020

@author: 33633
"""
import pygame

size=750  # taille de la fenetre
nb_case=15 # nombre de cases
resize_decor=int(size/nb_case) # taille des sprites

maze_name='labyrinthe1' #nom de l'onglet du classeur excel

'''
chargement et redimensionnement des sprites
'''
needle=pygame.transform.scale(pygame.image.load('ressource/aiguille.png'),(resize_decor,resize_decor))
syringe=pygame.transform.scale(pygame.image.load('ressource/seringue.png'),(resize_decor,resize_decor))
ether=pygame.transform.scale(pygame.image.load('ressource/ether.png'),(resize_decor,resize_decor))
macgyver=pygame.transform.scale(pygame.image.load('ressource/MacGyver.png'),(resize_decor,resize_decor))
gardien=pygame.transform.scale(pygame.image.load('ressource/Gardien.png'),(resize_decor,resize_decor))
wall=pygame.transform.scale(pygame.image.load('ressource/wall.png'),(resize_decor,resize_decor))        
floor=pygame.transform.scale(pygame.image.load('ressource/floor.png'),(resize_decor,resize_decor))

victoire = pygame.transform.scale(pygame.image.load('ressource/victoire.jpg'),(600,600))
rip = pygame.transform.scale(pygame.image.load('ressource/rip.jpg'),(600,600))
