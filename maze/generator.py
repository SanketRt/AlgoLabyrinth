import numpy as np
import random

def generate_maze(width: int, height: int) -> np.ndarray:
    """
    Generate a perfect maze of size (height × width).
    Maze is represented as a boolean array:
      True  = wall
      False = corridor
    Requirements: width and height should be odd.
    """
    # Start with all walls
    maze = np.ones((height, width), dtype=bool)
    random.seed(1)
    def carve(r: int, c: int):
        maze[r, c] = False
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        random.shuffle(directions)
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 < nr < height and 0 < nc < width and maze[nr, nc]:
                maze[r + dr//2, c + dc//2] = False
                carve(nr, nc)

    carve(1, 1)
    return maze


if __name__ == "__main__":
    W, H = 21, 15  
    m = generate_maze(W, H)
    print("Maze shape:", m.shape)
    for row in m:
        print("".join("█" if cell else " " for cell in row))
