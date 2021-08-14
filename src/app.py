import random
from time import perf_counter_ns
from typing import Set

import pygame

from . import FPS_LIMIT, TITLE, screen, viewport,  SCREEN_SIZE
from .classes.tiles import Tile
from .classes.camera import camera


class App:

    def __init__(self) -> None:
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.is_running: bool = True

        self.debug = False
        self.fps_limit = FPS_LIMIT

        self.pressed: Set[int] = set()

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.QUIT:
            self.is_running = False

        elif event.type == pygame.KEYDOWN:
            self.pressed.add(event.key)

            if event.key == pygame.K_f:
                self.toggle_debug_mode()

        elif event.type == pygame.KEYUP:
            self.pressed.remove(event.key)

    def toggle_debug_mode(self):
        if self.debug:
            self.debug = False
            self.fps_limit = FPS_LIMIT
            pygame.display.set_caption(TITLE)

        else:
            self.debug = True
            # The more fps, the more cpu usage
            self.fps_limit = 1000

    def run(self) -> None:
        tiles = [
            [
                Tile(
                    random.choice(list(Tile.SPRITES.keys())),
                    (x * Tile.SIZE - camera.x, y * Tile.SIZE - camera.y)
                ) for x in range(Tile.TILE_COUNT_X)
            ] for y in range(Tile.TILE_COUNT_Y)
        ]

        while self.is_running:
            marker: float = perf_counter_ns()

            # Temporary white bg to simulate scratch background.
            viewport.fill((255, 255, 255))

            camera.update(self.pressed)

            for line in tiles:
                for tile in line:
                    tile.update(camera)

                    viewport.blit(
                        tile.sprite,
                        (
                            tile.rect.x - camera.x,
                            tile.rect.y - camera.y
                        )
                    )

            screen.blit(pygame.transform.scale(viewport, SCREEN_SIZE), (0, 0))
            pygame.display.update()

            for event in pygame.event.get():
                self.handle_event(event)

            if self.debug:
                pygame.display.set_caption(
                    f"{TITLE} - {self.clock.get_fps():.0f} fps "
                    f"- {(perf_counter_ns() - marker) / 1000:.0f} µs"
                )

            self.clock.tick(self.fps_limit)

    def __del__(self) -> None:
        pygame.display.quit()
        pygame.quit()
