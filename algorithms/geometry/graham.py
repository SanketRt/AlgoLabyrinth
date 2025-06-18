from algorithms.geometry.jarvis import orientation

import math

def dist(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

def graham_scan(points):
    P = sorted(points, key=lambda p: (p[1], p[0]))  # lowest y, then x
    pivot = P[0]
    sorted_pts = P[1:]
    sorted_pts.sort(key=lambda p: (math.atan2(p[1]-pivot[1], p[0]-pivot[0]), dist(pivot, p)))

    stack = [pivot]
    yield {"points": P, "hull": stack.copy(),"current": pivot, "action":"push"}

    for pt in sorted_pts:
        yield {"points": P, "hull": stack.copy(),"current": pt, "action":"consider"}
        while len(stack) >= 2:
            o = orientation(stack[-2], stack[-1], pt)
            yield {"points": P, "hull": stack.copy(),"current": pt, "action":"compare"}
            if o <= 0:
                removed = stack.pop()
                yield {"points": P, "hull": stack.copy(),"current": pt, "action":"pop"}
            else:
                break
        stack.append(pt)
        yield {"points": P, "hull": stack.copy(),"current": pt, "action":"push"}

    yield {"points": P, "hull": stack.copy(), "action":"done"}
