import pygame
import random

class Grid:
    COLORS = [
        (50, 0, 1, 0.5),
        (80, 255, 80, 0.5),
        (255, 80, 255, 0.5),
        (255, 150, 0, 0.5),
    ]
    def __init__(self, column_count: int, row_count: int, scattered: bool = False):
        self.column_count = column_count
        self.row_count = row_count
        if scattered:
            self.values = [([random.choice([0, 1]) for _ in range(column_count)]
                            ) for _ in range(row_count)]
        else:
            self.values = [[0] * column_count for _ in range(row_count)]

    def read_value(self, x: int, y: int):
        return self.values[y][x]

    def write_value(self, x: int, y: int, value: int):
        self.values[y][x] = value

    def display(self, screen: pygame.Surface):
        gridSurface = pygame.Surface(screen.get_size())
        gridSurface.set_alpha(128)
        gridSurface.fill((0, 0, 0))
        width = screen.get_width()
        height = screen.get_height()
        unitX = width / self.column_count
        unitY = height / self.row_count
        for j in range(self.row_count):
            for i in range(self.column_count):
                value = self.read_value(i, j)
                color = Grid.COLORS[value]
                pygame.draw.rect(
                    surface=gridSurface,
                    color=color,
                    rect=(i * unitX, j * unitY, unitX - 1, unitY - 1),
                    width=0
                )
        screen.blit(gridSurface, (0, 0))

    def display_beaver(self, screen: pygame.Surface, x: int, y: int, color: tuple):
        width = screen.get_width()
        height = screen.get_height()
        unitX = width / self.column_count
        unitY = height / self.row_count
        pygame.draw.rect(
            surface=screen,
            color=color,
            rect=(x * unitX, y * unitY, unitX, unitY),
            width=0
        )
