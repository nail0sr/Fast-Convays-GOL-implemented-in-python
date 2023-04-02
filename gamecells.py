import pygame
import random
from collections import defaultdict
from collections import namedtuple
pygame.init()
RED =[255, 0, 0]
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
win_size = [400, 400]
SCREEN = pygame.display.set_mode(win_size)
SCREEN.fill(BLACK)
CLOCK = pygame.time.Clock()
fps = 20
game = True
cell =namedtuple("cell", ["x", "y"])
some_cell = defaultdict(bool)
cells = set()
for i in range(60):
    i, e = random.randrange(1, 21), random.randrange(1, 21)
    cells.add(cell(i, e))
for i in cells:
    print(i)
def main():
    while game:
        draw_grid(win_size=win_size)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        for i in range(1, 21):
            for e in range(1, 21):
                if cell(i, e) in cells:
                    draw_cell(i*20, e*20)
                    nbrs = 0
                    checks = [(i-1, e-1), (i, e-1), (i+1, e-1),
                              (i-1, e), (i+1, e),
                              (i-1, e+1), (i, e+1), (i+1, e+1)]
                    for check in checks:
                        if cell(check[0], check[1]) in cells:
                            nbrs+=1
                    if nbrs < 2 or nbrs > 3:
                        cells.remove(cell(i, e))
                        kill_cell(i*20, e*20)
                else:
                    nbrs = 0
                    checks=[(i-1, e-1), (i, e-1), (i+1, e-1),
                              (i-1, e), (i+1, e),
                              (i-1, e+1), (i, e+1), (i+1, e+1)]
                    for check in checks:
                        if cell(check[0], check[1]) in cells:
                            nbrs+=1
                    if nbrs == 3:
                        cells.add(cell(i, e))
                        draw_cell(i*20, e*20)

        CLOCK.tick(fps)
        pygame.display.update()

                
def kill_cell(x, y):
    rect = pygame.Rect(x, y, 20, 20)
    pygame.draw.rect(SCREEN, BLACK, rect, 10)
def draw_grid(win_size):
    for x in range(0, win_size[0], 20):
        for y in range(0, win_size[1], 20):
            rect = pygame.Rect(x, y, 20, 20)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)
def draw_cell(x, y):
    rect =pygame.Rect(x, y, 20, 20)
    pygame.draw.rect(SCREEN, RED, rect, 10)
if __name__ == "__main__":
    main()