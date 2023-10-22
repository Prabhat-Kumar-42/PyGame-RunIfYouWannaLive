import pygame
from sys import exit

pygame.init() #pygame.init() initializes pygame
pygame.display.set_caption('speed')

clock = pygame.time.Clock() #clock obj, helps with time and controlling framerate

width = 800
height = 400
screen = pygame.display.set_mode((width, height))

'''
---------- Code for creating and adding color to test surface ---------------
test_surface_width = 100
test_surface_height = 200
test_surface = pygame.Surface((test_surface_width, test_surface_height)) # create regular surface
test_surface.fill('White') # fill the surface with a color
'''
 #code for loading an image to a surface
sky_surface = pygame.image.load('./graphics/Sky.png')

while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # pygame.QUIT is synonomus to close button(x) button in display screen  
            pygame.quit()             # pygame.quit() uninitializes pygame, it's basically opposite of pygame.init() 
            exit()                    # exit() from sys module closes any kind of code once it's called
    # draw all our elements
    # update everything

    # attach and display the test_surface to display surface, bli stands for block image transfer (fancy way of saying put one surface on another surface)
    screen.blit(sky_surface , (0,0)) #(surface, position) 

    pygame.display.update() # update the display surface, in our case screen
    clock.tick(60) # set upperlimit for framerate as 60 fps
