import pygame

from . import FPS_LIMIT


class App:

    def __init__(self) -> None:
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.is_running: bool = True

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.QUIT:
            self.is_running = False

    def run(self) -> None:
        while self.is_running:
            for event in pygame.event.get():
                self.handle_event(event)

            pygame.display.update()
            self.clock.tick(FPS_LIMIT)

    def __del__(self) -> None:
        pygame.display.quit()
        pygame.quit()
