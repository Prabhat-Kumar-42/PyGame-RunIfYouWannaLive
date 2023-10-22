import pygame
from sys import exit

def display_score(program_start_time):
    current_time = round(pygame.time.get_ticks()/1000 - program_start_time, 2) 
    score_surface = surface_font.render("Score: ", False, "Dark Green")
    score_rectangle = score_surface.get_rect(midright = (700, 50))
    screen.blit(score_surface, score_rectangle)
    time_surface = surface_font.render(str(current_time), False, "Dark Green")
    time_rectangle = time_surface.get_rect(midleft = (700, 50))
    screen.blit(time_surface, time_rectangle)

def initializeScreen():
    # attach and display the test_surface to display surface, bli stands for block image transfer (fancy way of saying put one surface on another surface)
    screen.blit(sky_surface , (0,0)) #(surface, position) 
    screen.blit(ground_surface, (0, 300))

def gameEndScreen():
    not_fast_enough_surface = surface_font.render("You Were Not Fast Enough !!", False, "White")
    not_fast_enough_rectangle = not_fast_enough_surface.get_rect(midtop = (400, 300))
    player_stand_surface = pygame.image.load('./graphics/Player/player_stand.png').convert_alpha()
    player_stand_surface = pygame.transform.rotozoom(player_stand_surface, 0, 2)
    player_stand_rectangle = player_stand_surface.get_rect(center = (400, 200))
    screen.blit(player_stand_surface, player_stand_rectangle)
    screen.blit(not_fast_enough_surface, not_fast_enough_rectangle)
    addInstructions()

def addInstructions():
    instruction_font = pygame.font.Font('./font/Pixeltype.ttf', 30)
    if start_screen:
        instructions_surface = instruction_font.render('Press Space to Start the Game', False, "Dark Green")
    else:
        instructions_surface = instruction_font.render('Press Space to Restart the Game', False, "White")
    instructions_rectangle = instructions_surface.get_rect(midtop = (400, 80))
    screen.blit(instructions_surface, instructions_rectangle)

def addTitle():
    title_surface = surface_font.render('Run If You Wanna Live', False, 'Dark Green').convert()
    title_rectangle = title_surface.get_rect(center = (400, 50))
    screen.blit(title_surface, title_rectangle)
    addInstructions()

pygame.init()                                       #pygame.init() initializes pygame
pygame.display.set_caption('Run If You Wanna Live') # Add Title to the Game Window
clock = pygame.time.Clock()                         #clock obj, helps with time and controlling framerate
program_start_time = 0
game_active = False                                 #boolean to check if game is over or not
width = 800
height = 400
screen = pygame.display.set_mode((width, height))
start_screen = True
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

#score_surface
surface_font = pygame.font.Font('./font/Pixeltype.ttf', 50) # creating font object to create a font surface
#snail
snail_surface = pygame.image.load('./graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 800
snail_y_pos = 300 
snail_rectangle = snail_surface.get_rect(midbottom = (snail_x_pos,snail_y_pos))

#player
player_surface = pygame.image.load('./graphics/Player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom= (80, 300)) 
player_gravity = 0

while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # pygame.QUIT is synonomus to close button(x) button in display screen  
            pygame.quit()             # pygame.quit() uninitializes pygame, it's basically opposite of pygame.init() 
            exit()                    # exit() from sys module closes any kind of code once it's called
        if game_active:
            if program_start_time == 0:
                program_start_time = pygame.time.get_ticks()/1000
            if player_rectangle.bottom >= 300:
                if event.type == pygame.KEYDOWN:
                    #print('key down')
                    if event.key == pygame.K_SPACE: 
                        player_gravity = -20

                if event.type == pygame.MOUSEBUTTONDOWN:
                    #print('mouse down')
                    if player_rectangle.collidepoint(event.pos) and player_rectangle.bottom >= 300:
                        player_gravity = -20
        else:
            if((event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) 
                or event.type == pygame.MOUSEBUTTONDOWN):
                game_active = True
                snail_rectangle.left = 800
                program_start_time = 0 
        # draw all our elements
    # update everything
    
    if game_active :
        start_screen = False
        initializeScreen()   
        display_score(program_start_time)

        #pygame.draw.rect(screen, '#c0e8ec', score_rectangle)
        #pygame.draw.rect(screen, '#c0e8ec', score_rectangle, 1)

        # reset snail position so it re-appears after it reaches it's end position
        if(snail_rectangle.right < 0):
            snail_rectangle.left = 800
        screen.blit(snail_surface, snail_rectangle)
        snail_rectangle.left = snail_rectangle.left-4 #changes so snail appeares to be moving along x_pos
    
        #player
        player_gravity = player_gravity + 1
        player_rectangle.y += player_gravity
        if(player_rectangle.bottom >= 300):
            player_rectangle.bottom = 300
        screen.blit(player_surface, player_rectangle)
   
        #collision
        if snail_rectangle.colliderect(player_rectangle):
            game_active = False
   #if player_rectangle.colliderect(snail_rectangle):
    #    print("Collision")

    #mouse_pos = pygame.mouse.get_pos()
    #if ( player_rectangle.collidepoint(mouse_pos)):
    #    print("collision")
    elif start_screen:
        initializeScreen()
        addTitle()
        #gameEndScreen()
        player_rectangle.bottom = 300
        player_rectangle.left = 80
        screen.blit(player_surface, player_rectangle)
    else:
        screen.fill((94, 129, 162))
        gameEndScreen()

    pygame.display.update() # update the display surface, in our case screen
    clock.tick(60) # set upperlimit for framerate as 60 fps
