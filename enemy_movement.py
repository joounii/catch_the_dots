from dis import dis
import pygame
import math

def move_enemy(enemy_x, enemy_y, player_x, player_y, pursuit_speed):

    distance_x = player_x - enemy_x
    distance_y = player_y - enemy_y

    # Calculate the angle between the enemy and the player
    angle = math.atan2(distance_y, distance_x)

    # Calculate the enemy's new position based on the angle and a pursuit speed
    
    enemy_x += math.cos(angle) * pursuit_speed
    enemy_y += math.sin(angle) * pursuit_speed

    return enemy_x, enemy_y