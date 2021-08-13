from typing import Tuple

import pygame

pygame.init()


WIDTH: int = 960
HEIGHT: int = 720
SCREEN_SIZE: Tuple[int, int] = (WIDTH, HEIGHT)

FPS_LIMIT: int = 60

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Tile Scrolling Platformer')
icon = pygame.image.load('assets/icon.png').convert_alpha()
pygame.display.set_icon(icon)
