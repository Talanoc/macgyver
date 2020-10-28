# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 10:40:13 2020

@author: 33633
"""
import pygame
# taille de la fenetre
size = 750
# nombre de cases
nb_case = 15
# taille des sprites
resize_decor = int(size/nb_case)
# nom de l'onglet du classeur excel
maze_name = 'labyrinthe1'

'''
chargement et redimensionnement des sprites
'''
needle = pygame.transform.scale(pygame.image.load('ressource/aiguille.png'),
                                (resize_decor, resize_decor))
syringe = pygame.transform.scale(pygame.image.load('ressource/seringue.png'),
                                 (resize_decor, resize_decor))
ether = pygame.transform.scale(pygame.image.load('ressource/ether.png'),
                               (resize_decor, resize_decor))
macgyver = pygame.transform.scale(pygame.image.load('ressource/MacGyver.png'),
                                  (resize_decor, resize_decor))
gardien = pygame.transform.scale(pygame.image.load('ressource/Gardien.png'),
                                 (resize_decor, resize_decor))
wall = pygame.transform.scale(pygame.image.load('ressource/wall.png'),
                              (resize_decor, resize_decor))
floor = pygame.transform.scale(pygame.image.load('ressource/floor.png'),
                               (resize_decor, resize_decor))

victoire = pygame.transform.scale(pygame.image.load('ressource/victoire.jpg'),
                                  (600, 600))
rip = pygame.transform.scale(pygame.image.load('ressource/rip.jpg'),
                             (600, 600))
