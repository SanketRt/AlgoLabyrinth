import pygame
import sys
import time
from maze.generator import generate_maze
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.dijkstra import dijkstra
from algorithms.astar import astar
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "100,200"

CELL_SIZE = 12  # pixel size of each maze cell
MAZE_WIDTH, MAZE_HEIGHT = 41, 31  
START = (1, 1)
GOAL = (MAZE_HEIGHT - 2, MAZE_WIDTH - 2)

COLOR_WALL = (0, 0, 0)
COLOR_FREE = (255, 255, 255)
COLOR_EXPLORE = (100, 200, 255)
COLOR_PATH = (255, 200, 0)
COLOR_TEXT_BG = (30, 30, 30)
COLOR_TEXT = (240, 240, 240)

SOLVERS = [
    ("BFS", bfs),
    ("DFS", dfs),
    ("Dijkstra", dijkstra),
    ("A*", astar),
]
QUADS = [ (0,0), (1,0), (0,1), (1,1) ]

pygame.init()
screen = pygame.display.set_mode(
    (2 * MAZE_WIDTH * CELL_SIZE, 2 * MAZE_HEIGHT * CELL_SIZE)
)
pygame.display.set_caption("Maze Solver Comparison")
font = pygame.font.SysFont(None, 20)

maze = generate_maze(MAZE_WIDTH, MAZE_HEIGHT)

results = {}
max_steps = 0
for (name, fn) in SOLVERS:
    path, order = fn(maze, START, GOAL)
    results[name] = { 'path': path, 'order': order }
    max_steps = max(max_steps, len(order))

clock = pygame.time.Clock()
step = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if step <= max_steps:
        screen.fill((50,50,50))

        for idx, (name, _) in enumerate(SOLVERS):
            quad_x, quad_y = QUADS[idx]
            ox = quad_x * MAZE_WIDTH * CELL_SIZE
            oy = quad_y * MAZE_HEIGHT * CELL_SIZE

            for r in range(MAZE_HEIGHT):
                for c in range(MAZE_WIDTH):
                    color = COLOR_WALL if maze[r,c] else COLOR_FREE
                    rect = (ox + c*CELL_SIZE, oy + r*CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    pygame.draw.rect(screen, color, rect)

            data = results[name]
            for i in range(min(step, len(data['order']))):
                r,c = data['order'][i]
                rect = (ox + c*CELL_SIZE, oy + r*CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, COLOR_EXPLORE, rect)

            if step >= len(data['order']):
                for (r,c) in data['path']:
                    rect = (ox + c*CELL_SIZE, oy + r*CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    pygame.draw.rect(screen, COLOR_PATH, rect)

            label_bg = pygame.Rect(ox, oy, MAZE_WIDTH*CELL_SIZE, 20)
            pygame.draw.rect(screen, COLOR_TEXT_BG, label_bg)
            text = font.render(f"{name}", True, COLOR_TEXT)
            screen.blit(text, (ox + 5, oy + 2))

        step += 1

    pygame.display.flip()
    clock.tick(60) 

pygame.quit()
sys.exit()