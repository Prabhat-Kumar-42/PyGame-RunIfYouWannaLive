import pygame
from sys import exit

pygame.init() #pygame.init() initializes pygame

width = 800
height = 400
 
screen = pygame.display.set_mode((width, height))
while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # pygame.QUIT is synonomus to close button(x) button in display screen  
            pygame.quit()             # pygame.quit() uninitializes pygame, it's basically opposite of pygame.init() 
            exit()                    # exit() from sys module closes any kind of code once it's called
    # draw all our elements
    # update everything
    pygame.display.update() # update the display surface, in our case screen
