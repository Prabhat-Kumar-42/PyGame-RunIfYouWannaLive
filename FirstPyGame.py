import pygame
from sys import exit

#pygame.init() initializes pygame
pygame.init() 

# Add Title to the Game Window
pygame.display.set_caption('Run If You Wanna Live')

#clock obj, helps with time and controlling framerate
clock = pygame.time.Clock() 

width = 800
height = 400
screen = pygame.display.set_mode((width, height))

#---------- Code for creating and adding color to test surface ---------------
#test_surface_width = 100
#test_surface_height = 200
#test_surface = pygame.Surface((test_surface_width, test_surface_height)) # create regular surface
#test_surface.fill('White') # fill the surface with a color
#

#code for loading an image to a surface
# .convert() converts the loaded image to something native that pygame can easily render, 
#i.e, it speeds up pygame working
sky_surface = pygame.image.load('./graphics/sky.png').convert()
ground_surface = pygame.image.load('./graphics/ground.png').convert()
surface_font = pygame.font.Font('./font/Pixeltype.ttf', 50) # creating font object to create a font surface
text_surface = surface_font.render('Run If You Wanna Live', False, 'Dark Green').convert()

#snail
snail_surface = pygame.image.load('./graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 800
snail_y_pos = 300 
snail_rectangle = snail_surface.get_rect(midbottom = (snail_x_pos,snail_y_pos))

#player
player_surface = pygame.image.load('./graphics/Player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom= (80, 300)) 

while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # pygame.QUIT is synonomus to close button(x) button in display screen  
            pygame.quit()             # pygame.quit() uninitializes pygame, it's basically opposite of pygame.init() 
            exit()                    # exit() from sys module closes any kind of code once it's called
    # draw all our elements
    # update everything

    # attach and display the test_surface to display surface, bli stands for block image transfer (fancy way of saying put one surface on another surface)
    screen.blit(sky_surface , (0,0)) #(surface, position) 
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (250, 100))

    # reset snail position so it re-appears after it reaches it's end position
    if(snail_rectangle.right < 0):
        snail_rectangle.left = 800
    screen.blit(snail_surface, snail_rectangle)
    snail_rectangle.left = snail_rectangle.left-4 #changes so snail appeares to be moving along x_pos

    screen.blit(player_surface, player_rectangle)

    pygame.display.update() # update the display surface, in our case screen
    clock.tick(60) # set upperlimit for framerate as 60 fps
