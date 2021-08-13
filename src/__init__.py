from .functions.loaders import load_sprites_from_dir
from typing import Tuple

import pygame

pygame.init()

WIDTH: int = 960
HEIGHT: int = 720
SCREEN_SIZE: Tuple[int, int] = (WIDTH, HEIGHT)

FPS_LIMIT: int = 60
TITLE: str = "Tile Scrolling Platformer"

ASSETS_FOLDER: str = 'assets'
TEXTURES_FOLDER: str = f'{ASSETS_FOLDER}/textures'

screen: pygame.display = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption(TITLE)
icon: pygame.Surface = pygame.image.load("assets/icon.png").convert_alpha()
pygame.display.set_icon(icon)

TILE_SIZE = 32
TILE_SPRITES = load_sprites_from_dir(
    f"{TEXTURES_FOLDER}/tiles",
    (
        "block_gold",
    )
)
