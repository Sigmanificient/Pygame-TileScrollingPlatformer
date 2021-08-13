from typing import Tuple

import pygame

pygame.init()

WIDTH: int = 960
HEIGHT: int = 720
SCREEN_SIZE: Tuple[int, int] = (WIDTH, HEIGHT)

FPS_LIMIT: int = 60
TITLE: str = "Tile Scrolling Platformer"

screen: pygame.display = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption(TITLE)
icon: pygame.Surface = pygame.image.load("assets/icon.png").convert_alpha()
pygame.display.set_icon(icon)
