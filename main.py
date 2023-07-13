import pygame
import time
from grid import *
from turing import *

def main():
    pygame.init()
    logo = pygame.image.load("logo.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Simulation")
    screen = pygame.display.set_mode((900, 900), pygame.NOFRAME)

    cols = 200
    rows = cols
    updates_per_turn = 5
    code_complexity = 100
    grid = Grid(cols, rows)
    turingA = TuringMachine(random.randint(0, cols-1), random.randint(0, rows-1), code_complexity)
    turingB = TuringMachine(random.randint(0, cols-1), random.randint(0, rows-1), code_complexity)
    turingC = TuringMachine(random.randint(0, cols-1), random.randint(0, rows-1), code_complexity)

    # GAME LOOP
    running = True
    while running:
        # Quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False
        
        # Update
        for _ in range(updates_per_turn):
            turingA.update(grid, 1)
            turingB.update(grid, 2)
            turingC.update(grid, 3)
        
        # Display
        screen.fill((0, 0, 0))
        grid.display(screen)
        grid.display_turing_machine(screen, turingA.x, turingA.y, (255, 0, 0))
        grid.display_turing_machine(screen, turingB.x, turingB.y, (0, 0, 255))
        grid.display_turing_machine(screen, turingC.x, turingC.y, (255, 255, 0))
        pygame.display.update()

        # Sleep
        # time.sleep(0.1)
     
if __name__=="__main__":
    main()