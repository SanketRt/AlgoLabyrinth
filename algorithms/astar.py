import heapq
import math

def heuristic(u, goal):
    return abs(u[0] - goal[0]) + abs(u[1] - goal[1])

def astar(grid, start, goal):
    h, w = grid.shape
    g_score = {start: 0}
    parent = {}
    order = []
    visited = set()
    pq = [(heuristic(start, goal), start)]

    while pq:
        f, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        order.append(u)
        if u == goal:
            break

        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            v = (u[0] + dr, u[1] + dc)
            if not (0 <= v[0] < h and 0 <= v[1] < w):
                continue
            if grid[v]:  
                continue

            tentative = g_score[u] + 1
            if tentative < g_score.get(v, float('inf')):
                g_score[v] = tentative
                parent[v] = u
                f_score = tentative + heuristic(v, goal)
                heapq.heappush(pq, (f_score, v))

    path = []
    if goal in parent or start == goal:
        cur = goal
        while cur != start:
            path.append(cur)
            cur = parent[cur]
        path.append(start)
        path.reverse()

    return path, order

if __name__ == "__main__":
    import numpy as np
    g = np.zeros((7,7), dtype=bool)
    p, order = astar(g, (0,0), (6,6))
    print("A* Path:", p)
    print("Expansion Order:", order)
