import math
from typing import Dict

import pygame

from src import TEXTURES_FOLDER, HALF_WIDTH, HALF_HEIGHT
from src.functions.loaders import load_sprites_from_dir


class Tile:
    SIZE: int = 32
    TILE_COUNT_X: int = math.ceil(HALF_WIDTH / SIZE) + 1
    TILE_COUNT_Y: int = math.ceil(HALF_HEIGHT / SIZE) + 1

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

    def update(self, camera):
        if self.rect.x - camera.x < -self.SIZE:
            self.rect.x += self.SIZE * self.TILE_COUNT_X

        elif self.rect.x - camera.x > HALF_WIDTH:
            self.rect.x -= self.SIZE * self.TILE_COUNT_X

        elif self.rect.y - camera.y < -self.SIZE:
            self.rect.y += self.SIZE * self.TILE_COUNT_Y

        elif self.rect.y - camera.y > HALF_HEIGHT:
            self.rect.y -= self.SIZE * self.TILE_COUNT_Y

    @property
    def sprite(self):
        return self.SPRITES[self.name]
