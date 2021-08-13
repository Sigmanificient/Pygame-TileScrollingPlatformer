from time import perf_counter_ns
from typing import Set

import pygame

from . import FPS_LIMIT, TITLE, screen


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
                self.debug = not self.debug

                self.fps_limit = 1000 if self.debug else FPS_LIMIT

                if not self.debug:
                    pygame.display.set_caption(TITLE)

        elif event.type == pygame.KEYUP:
            self.pressed.remove(event.key)

    def run(self) -> None:
        while self.is_running:
            marker = perf_counter_ns()

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
