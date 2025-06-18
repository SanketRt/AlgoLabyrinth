import pygame
import imageio
import numpy as np
import time
import random
from copy import deepcopy

# ---- Sudoku Generator & Backtracking ----
def valid(board, row, col, num):
    # check row, column, and 3x3 box
    if any(board[row][x] == num for x in range(9)):
        return False
    if any(board[y][col] == num for y in range(9)):
        return False
    br, bc = 3 * (row // 3), 3 * (col // 3)
    for r in range(br, br + 3):
        for c in range(bc, bc + 3):
            if board[r][c] == num:
                return False
    return True


def fill_board(board):
    # fill a complete board with backtracking
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                nums = list(range(1, 10))
                random.shuffle(nums)
                for num in nums:
                    if valid(board, i, j, num):
                        board[i][j] = num
                        if fill_board(board):
                            return True
                board[i][j] = 0
                return False
    return True


def generate_easy_puzzle(removals=25):
    board = [[0]*9 for _ in range(9)]
    fill_board(board)
    solution = deepcopy(board)
    cells = random.sample([(r, c) for r in range(9) for c in range(9)], removals)
    for r, c in cells:
        board[r][c] = 0
    return board, solution

def generate_med_puzzle(removals=35):
    board = [[0]*9 for _ in range(9)]
    fill_board(board)
    solution = deepcopy(board)
    cells = random.sample([(r, c) for r in range(9) for c in range(9)], removals)
    for r, c in cells:
        board[r][c] = 0
    return board, solution

def solve_sudoku(board):
    """
    Backtracking generator: yields (board, (row, col), action)
    action: 'place', 'remove', 'done'
    """
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if valid(board, i, j, num):
                        board[i][j] = num
                        yield deepcopy(board), (i, j), 'place'
                        for frame in solve_sudoku(board):
                            yield frame
                        # if solved, end recursion
                        if all(all(cell != 0 for cell in row) for row in board):
                            return
                        board[i][j] = 0
                        yield deepcopy(board), (i, j), 'remove'
                return
    yield deepcopy(board), (None, None), 'done'

# ---- Visualization ----
def main():
    pygame.init()
    SIZE = 540  # 60px per cell
    MARGIN = 20
    WIDTH, HEIGHT = SIZE + 2 * MARGIN, SIZE + 2 * MARGIN
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Sudoku Solver Visualization (Medium)')
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 40)
    small = pygame.font.SysFont(None, 24)
    FPS = 10

    puzzle, solution = generate_med_puzzle(removals=40)
    frames = list(solve_sudoku(deepcopy(puzzle)))

    gif_frames = []
    start_time = time.time()
    step = 0
    running = True
    cell = SIZE // 9

    while running and step < len(frames):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
        board, (r, c), action = frames[step]

        screen.fill((255, 255, 255))
        # draw grid lines
        for i in range(10):
            thickness = 4 if i % 3 == 0 else 1
            pygame.draw.line(screen, (0, 0, 0), (MARGIN + i*cell, MARGIN), (MARGIN + i*cell, MARGIN + SIZE), thickness)
            pygame.draw.line(screen, (0, 0, 0), (MARGIN, MARGIN + i*cell), (MARGIN + SIZE, MARGIN + i*cell), thickness)

        # draw numbers
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != 0:
                    color = (0, 0, 255) if puzzle[i][j] == 0 else (0, 0, 0)
                    txt = font.render(str(num), True, color)
                    x = MARGIN + j*cell + cell//2 - txt.get_width()//2
                    y = MARGIN + i*cell + cell//2 - txt.get_height()//2
                    screen.blit(txt, (x, y))

        # highlight current cell
        if r is not None:
            pygame.draw.rect(screen, (255, 0, 0), (MARGIN + c*cell, MARGIN + r*cell, cell, cell), 3)

        # timer
        elapsed = int(time.time() - start_time)
        timer_s = small.render(f"Time: {elapsed}s", True, (0, 0, 0))
        screen.blit(timer_s, (MARGIN, HEIGHT - MARGIN - timer_s.get_height()))

        pygame.display.flip()
        # capture frame
        gif_frames.append(np.transpose(pygame.surfarray.array3d(screen), (1, 0, 2)))
        clock.tick(FPS)
        step += 1

    # Save GIF
    imageio.mimsave('sudoku_solver_med.gif', gif_frames, fps=FPS)
    print("GIF saved to sudoku_solver_med.gif")
    pygame.quit()

if __name__ == '__main__':
    main()
