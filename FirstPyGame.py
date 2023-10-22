import pygame
from sys import exit
from random import randint

def display_score(program_start_time):
    current_time = round(pygame.time.get_ticks()/1000 - program_start_time, 2) 
    score_surface = surface_font.render("Score: ", False, "Dark Green")
    score_rectangle = score_surface.get_rect(midright = (700, 50))
    screen.blit(score_surface, score_rectangle)
    time_surface = surface_font.render(str(current_time), False, "Dark Green")
    time_rectangle = time_surface.get_rect(midleft = (700, 50))
    screen.blit(time_surface, time_rectangle)
    return current_time

def initializeScreen():
    # attach and display the test_surface to display surface, bli stands for block image transfer (fancy way of saying put one surface on another surface)
    screen.blit(sky_surface , (0,0)) #(surface, position) 
    screen.blit(ground_surface, (0, 300))

def gameEndScreen(current_score):
    not_fast_enough_surface = surface_font.render("Your Score is " + str(current_score), False, "White")
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

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rectangle in obstacle_list:
           obstacle_rectangle.x -= 5
           if obstacle_rectangle.bottom == 300:
               screen.blit(snail_surface, obstacle_rectangle)
           else:
               screen.blit(fly_surface, obstacle_rectangle)
        
        obstacle_list = [obstacle_rectangle for obstacle_rectangle in obstacle_list if obstacle_rectangle.x > 0]
        return obstacle_list
    else:
        return []

def collisions(player, obstacle_list):
    if obstacle_list:
        for obstacle_rectangle in obstacle_list:
            if player.colliderect(obstacle_rectangle):
                return False 
    return True

def resetPlayerPosition():
    player_rectangle.bottom = 300
    player_rectangle.left = 80
    screen.blit(player_surface, player_rectangle)

def playerAnimations():
    global player_surface, player_index

    #play jump aniimation if the player is not on the floor
    if player_rectangle.bottom < 300 :
        player_surface = player_jump
    
    #play walk animation if the player is on the floor
    else:
        player_index += 0.1
        if player_index > 2:
            player_index = 0
        player_surface = player_walk[int(player_index)]

pygame.init()                                       #pygame.init() initializes pygame
pygame.display.set_caption('Run If You Wanna Live') # Add Title to the Game Window
clock = pygame.time.Clock()                         #clock obj, helps with time and controlling framerate
program_start_time = 0
game_active = False                                 #boolean to check if game is over or not
width = 800
height = 400
screen = pygame.display.set_mode((width, height))
start_screen = True
current_score = 0
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

#Obstacles
snail_frame_1 = pygame.image.load('./graphics/snail/snail1.png').convert_alpha()
snail_frame_2 = pygame.image.load('./graphics/snail/snail2.png').convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surface = snail_frames[snail_frame_index]

fly_frame_1 = pygame.image.load('./graphics/Fly/Fly1.png').convert_alpha()
fly_frame_2 = pygame.image.load('./graphics/Fly/Fly2.png').convert_alpha()
fly_frames = [fly_frame_1, fly_frame_2]
fly_frame_index = 0
fly_surface = fly_frames[fly_frame_index]

obstacle_list = []

#player
player_walk_1= pygame.image.load('./graphics/Player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('./graphics/Player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load('./graphics/Player/jump.png').convert_alpha()
player_surface = player_walk[player_index]
player_rectangle = player_surface.get_rect(midbottom= (80, 300)) 
player_gravity = 0

#TImers
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

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
            if event.type == obstacle_timer:
                if randint(0, 2):
                    obstacle_list.append(snail_surface.get_rect(bottomright = (randint(900, 1100), 300)))
                else:
                    obstacle_list.append(fly_surface.get_rect(bottomright = (randint(900, 1100), 190)))
            if event.type == snail_animation_timer:
                if snail_frame_index == 0:
                    snail_frame_index = 1
                else :
                    snail_frame_index = 0
                snail_surface = snail_frames[snail_frame_index]
            if event.type == fly_animation_timer:
                if fly_frame_index == 0:
                    fly_frame_index = 1
                else:
                    fly_frame_index = 0
                fly_surface = fly_frames[fly_frame_index]

        else:
            if((event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) 
                or event.type == pygame.MOUSEBUTTONDOWN):
                game_active = True
                program_start_time = 0 
        # draw all our elements
    # update everything
    
    if game_active :
        start_screen = False
        initializeScreen()   
        current_score = display_score(program_start_time)

        #pygame.draw.rect(screen, '#c0e8ec', score_rectangle)
        #pygame.draw.rect(screen, '#c0e8ec', score_rectangle, 1)

        # reset snail position so it re-appears after it reaches it's end position
        #if(snail_rectangle.right < 0):
        #    snail_rectangle.left = 800
        #screen.blit(snail_surface, snail_rectangle)
        #snail_rectangle.left = snail_rectangle.left-4 #changes so snail appeares to be moving along x_pos
   
        obstacle_list = obstacle_movement(obstacle_list)

        #player
        player_gravity = player_gravity + 1
        player_rectangle.y += player_gravity
        if(player_rectangle.bottom >= 300):
            player_rectangle.bottom = 300
        playerAnimations()
        screen.blit(player_surface, player_rectangle)
   
        #collision
        game_active = collisions(player_rectangle, obstacle_list) 
    #if player_rectangle.colliderect(snail_rectangle):
    #    print("Collision")

    #mouse_pos = pygame.mouse.get_pos()
    #if ( player_rectangle.collidepoint(mouse_pos)):
    #    print("collision")
    elif start_screen:
        initializeScreen()
        addTitle()
        resetPlayerPosition()
    else:
        obstacle_list.clear()
        player_gravity = 0
        resetPlayerPosition()
        screen.fill((94, 129, 162))
        gameEndScreen(current_score)

    pygame.display.update() # update the display surface, in our case screen
    clock.tick(60) # set upperlimit for framerate as 60 fps
