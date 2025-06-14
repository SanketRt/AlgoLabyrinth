import heapq

def dijkstra(grid, start, goal):

    h, w = grid.shape
    dist = {start: 0}
    parent = {}
    order = []
    visited = set()
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        order.append(u)
        if u == goal:
            break
        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            v = (u[0] + dr, u[1] + dc)
            if 0 <= v[0] < h and 0 <= v[1] < w and not grid[v]:
                nd = d + 1
                if nd < dist.get(v, float('inf')):
                    dist[v] = nd
                    parent[v] = u
                    heapq.heappush(pq, (nd, v))

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
    p, order = dijkstra(g, (0,0), (4,4))
    print("Dijkstra Path:", p)
    print("Visit Order:", order)