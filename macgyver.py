import pygame

fic= open("labyrinthe.xlsx","r")
fic.close()

"""
continuer = True            
while continuer:           
    for event in pygame.event.get():
        if event.type == pygame.KEYUP and event.key==K_UP:
            position_macgyver=position_macgyver-15
            if position_macgyver in floor_display:
                pass
            else:
                position_macgyver=position_macgyver+15
                
        elif event.type == pygame.KEYUP and event.key==K_DOWN:
            position_macgyver=position_macgyver+15
            if position_macgyver in floor_display:
                pass
            else:
                position_macgyver=position_macgyver-15 
                
        elif event.type == pygame.KEYUP and event.key==K_RIGHT:
            position_macgyver=position_macgyver+1
            if position_macgyver in floor_display:
                pass
            else:
                position_macgyver=position_macgyver-1
                
        elif event.type == pygame.KEYUP and event.key==K_LEFT:
            position_macgyver=position_macgyver-1
            if position_macgyver in floor_display:
                pass
            else:
                position_macgyver=position_macgyver+1
                
                
                 
        elif event.type == pygame.KEYUP and event.key==K_ESCAPE:
                continuer = False
            
            
        #screen.blit(macgyver, ( 0 , 0 ))    
        pygame.display.flip()
pygame.quit()

"""