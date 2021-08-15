from typing import Tuple, List

import pygame


def load_sprites_from_dir(
    directory: str, file_list: Tuple[str, ...]
) -> List[pygame.Surface]:
    """Return a dictionary of the map sprites from a given directory."""
    return [
        pygame.image.load(f'{directory}/{file_name}.png')
        for file_name in file_list
    ]
