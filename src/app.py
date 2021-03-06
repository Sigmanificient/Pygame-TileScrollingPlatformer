from typing import Set

import pygame

from . import FPS_LIMIT, TITLE, screen, viewport, SCREEN_SIZE
from .classes.camera import camera
from .classes.tiles import Tiles


class App:

    def __init__(self) -> None:
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.is_running: bool = True

        self.debug = False
        self.fps_limit = FPS_LIMIT

        self.pressed: Set[int] = set()
        self.tiles = Tiles(16, 13)

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

    def update(self):
        # Temporary white bg to simulate scratch background.
        viewport.fill((255, 255, 255))

        camera.update(self.pressed)
        self.tiles.draw(viewport, camera)

        screen.blit(pygame.transform.scale(viewport, SCREEN_SIZE), (0, 0))
        pygame.display.update()

        for event in pygame.event.get():
            self.handle_event(event)

    def run(self) -> None:
        while self.is_running:
            self.update()

            if self.debug:
                fps = self.clock.get_fps()

                pygame.display.set_caption(
                    f"{TITLE} - {fps:.0f} fps - {(1 / fps) * 1000:.1f} µs"
                )

            self.clock.tick(self.fps_limit)

    def __del__(self) -> None:
        pygame.display.quit()
        pygame.quit()
