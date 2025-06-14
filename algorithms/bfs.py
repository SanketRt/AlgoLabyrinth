from collections import deque

def bfs(grid, start, goal):
    h, w = grid.shape
    visited = set([start])
    parent = {}
    order = []
    q = deque([start])

    while q:
        u = q.popleft()
        order.append(u)
        if u == goal:
            break
        for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            v = (u[0] + dr, u[1] + dc)
            if (0 <= v[0] < h and 0 <= v[1] < w and not grid[v] and v not in visited):
                visited.add(v)
                parent[v] = u
                q.append(v)

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
    g = np.zeros((5,5), dtype=bool)
    p, order = bfs(g, (0,0), (4,4))
    print("Path:", p)
    print("Visited in order:", order)
