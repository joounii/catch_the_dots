import pygame

def get_image(image_name):
    return pygame.image.load("images/" + image_name).convert()