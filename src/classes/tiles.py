from typing import Dict

import pygame

from src import TEXTURES_FOLDER
from src.functions.loaders import load_sprites_from_dir


class Tile:
    SIZE: int = 32
    SPRITES: Dict[str, pygame.Surface] = load_sprites_from_dir(
        f"{TEXTURES_FOLDER}/tiles",
        (
            "wood_0", "wood_1", "wood_2", "wood_3", "wood_4", "wood_5",
            "block_gold", "block_wood",
            "blue_1", "blue_2", "blue_3", "blue_4",
            "blue_5", "blue_6", "blue_7", "blue_8", "blue_9"
        )
    )

    def __init__(self, name, coords):
        self.name = name
        self.rect = pygame.Rect(coords, (self.SIZE, self.SIZE))

    @property
    def sprite(self):
        return self.SPRITES[self.name]