from dis import dis
from hashlib import new
from turtle import distance
import pygame
import math

def move_enemy(player_x, player_y, enemy_x, enemy_y, speed):

    # calculate distance
    distance_x = player_x - enemy_x
    distance_y = player_y - enemy_y
    distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
    
    # calculate the "verhältniss" between the distanc_x and distanc_y
    verhältniss = distance / speed

    new_x = distance_x / verhältniss
    new_y = distance_y / verhältniss
    return new_x, new_y
