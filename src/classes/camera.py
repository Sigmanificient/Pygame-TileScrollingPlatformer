from dataclasses import dataclass

import pygame


@dataclass
class Camera:
    x: int
    y: int
    locked: bool

    def update(self, pressed):
        if pygame.K_UP in pressed:
            self.y -= 1

        if pygame.K_DOWN in pressed:
            self.y += 1

        if pygame.K_LEFT in pressed:
            self.x -= 1

        if pygame.K_RIGHT in pressed:
            self.x += 1


camera = Camera(0, 0, False)
