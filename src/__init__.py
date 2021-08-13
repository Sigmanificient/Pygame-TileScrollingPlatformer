from .functions.loaders import load_sprites_from_dir
from typing import Tuple, Dict

import pygame

pygame.init()

WIDTH: int = 960
HEIGHT: int = 720
SCREEN_SIZE: Tuple[int, int] = (WIDTH, HEIGHT)

HALF_WIDTH: int = WIDTH // 2
HALF_HEIGHT: int = HEIGHT // 2
VIEWPORT_SIZE: Tuple[int, int] = (HALF_WIDTH, HALF_HEIGHT)

FPS_LIMIT: int = 60
TITLE: str = "Tile Scrolling Platformer"

ASSETS_FOLDER: str = 'assets'
TEXTURES_FOLDER: str = f'{ASSETS_FOLDER}/textures'

screen: pygame.display = pygame.display.set_mode(SCREEN_SIZE)
viewport: pygame.Surface = pygame.Surface(VIEWPORT_SIZE)

pygame.display.set_caption(TITLE)
icon: pygame.Surface = pygame.image.load("assets/icon.png").convert_alpha()
pygame.display.set_icon(icon)

TILE_SIZE: int = 32
TILE_SPRITES: Dict[str, pygame.Surface] = load_sprites_from_dir(
    f"{TEXTURES_FOLDER}/tiles",
    (
        "wood_0",
        "wood_1",
        "wood_2",
        "wood_3",
        "wood_4",
        "wood_5",
        "block_gold",
        "block_wood",
        "blue_1",
        "blue_2",
        "blue_3",
        "blue_4",
        "blue_5",
        "blue_6",
        "blue_7",
        "blue_8",
        "blue_9"
    )
)
