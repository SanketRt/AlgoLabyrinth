def dfs(grid, start, goal):
    h, w = grid.shape
    visited = set()
    parent = {}
    order = []
    found = False

    def _dfs(u):
        nonlocal found
        if found:
            return
        visited.add(u)
        order.append(u)
        if u == goal:
            found = True
            return
        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            v = (u[0] + dr, u[1] + dc)
            if (0 <= v[0] < h and 0 <= v[1] < w and not grid[v] and v not in visited):
                parent[v] = u
                _dfs(v)

    _dfs(start)

    path = []
    if found or start == goal:
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
    p, order = dfs(g, (0,0), (4,4))
    print("DFS Path:", p)
    print("Visit Order:", order)
