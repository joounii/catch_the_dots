from ast import With
import imp
import pygame
import sys
import random
import math
from pygame.locals import *

# FILE IMPORTS START::
from start_variables import setup
from icon_factory import get_image
from enemy_movement import move_enemy
# FILE IMPORTS END::

# Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Game dimensions
WIDTH = 640
HEIGHT = 480

# START VARIABLES START::
start_variables = setup()

score = start_variables.get("score")
ghost_speed = start_variables.get("ghost_speed")
ghost_speedup = start_variables.get("ghost_speedup")
is_game_over = start_variables.get("is_game_over")
is_loop_running = start_variables.get("is_loop_running")
# START VARIABLES END::

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the font
font = pygame.font.Font(None, 36)

def exit():
    pygame.quit()
    sys.exit()
    
def set_up_ghosts(amount):
    # Set up the ghosts
    ghosts = []
    for i in range(amount):
        ghost_image = get_image("ghost.png")
        ghost_rect = ghost_image.get_rect()
        ghost_rect.x = 580
        ghost_rect.y = 420
        ghosts.append(ghost_rect)
        
    return (ghosts, ghost_image)
        
def set_up_coins(amount):
    # Set up the dots
    dot_image = get_image("dot.png")
    dot_image_width = 32
    dot_image_height = 32
    dots = []
    for i in range(amount):
        dot = dot_image.get_rect()
        dot.x = random.randrange(0 + dot_image_width, WIDTH - dot_image_width, 1)
        dot.y = random.randrange(0 + dot_image_height, HEIGHT - dot_image_height, 1)
        dots.append(dot)
        
    return (dots, dot_image)
    


def gameLoop(ghost_speed, score, is_game_over, is_loop_running):

    lose = False

    # Set up the clock
    clock = pygame.time.Clock()

    # Set up the player
    player_image = get_image("pacman.png")
    player_rect = player_image.get_rect()

    ghosts, ghost_image = set_up_ghosts(1)
    
    dots, dot_image= set_up_coins(10)
   

    # Set up the game loop
    while is_loop_running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        # Move the player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_rect.x -= 5
        if keys[pygame.K_RIGHT]:
            player_rect.x += 5
        if keys[pygame.K_UP]:
            player_rect.y -= 5
        if keys[pygame.K_DOWN]:
            player_rect.y += 5

        # check if player moves out of the map
        if player_rect.x <= -25:
            player_rect.x = WIDTH + 24
        if player_rect.x >= WIDTH + 25:
            player_rect.x = -24
        if player_rect.y <= -25:
            player_rect.y = HEIGHT + 24
        if player_rect.y >= HEIGHT + 25:
            player_rect.y = -24

        # Move the ghost/s
        for ghost_rect in ghosts:
            # TODO replace with ghost AI
            
            if player_rect.x > ghost_rect.x:
                ghost_rect.x += ghost_speed
            if player_rect.x < ghost_rect.x:
                ghost_rect.x -= ghost_speed
            if player_rect.y > ghost_rect.y:
                ghost_rect.y += ghost_speed
            if player_rect.y < ghost_rect.y:
                ghost_rect.y -= ghost_speed
            if ghost_rect.right > WIDTH:
                ghost_rect.left = 0
        
        
        # Draw the screen
        screen.fill(BLACK)
        screen.blit(player_image, player_rect)
        
        for ghost_rect in ghosts:
            screen.blit(ghost_image, ghost_rect)
            
        for dot in dots:
            screen.blit(dot_image, dot)
        pygame.display.flip()

        # check if player collided with ghost
        for ghost_rect in ghosts:
            if player_rect.colliderect(ghost_rect):
                lose = True
                print("You lose!")
                is_game_over = True
                pygame.quit()
                sys.exit()

        # check if player collided with coin
        for dot in dots:
            if player_rect.colliderect(dot):
                dots.remove(dot)

        # Check if player has won
        if not dots:
            if lose == False:
                print("You win!")
                score += 1
                print(score)
                ghost_speed += ghost_speedup
                gameLoop(ghost_speed, score, is_game_over, is_loop_running)

        # Limit the frame rate
        clock.tick(60)
        
if is_game_over == False:
    # game has been restarted with the start function
    gameLoop(ghost_speed, score, is_game_over, is_loop_running)

# Pygame closes game
pygame.quit()
