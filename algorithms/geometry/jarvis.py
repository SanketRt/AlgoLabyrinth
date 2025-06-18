import math

def orientation(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])

def jarvis_march(points):
    P = sorted(points) 
    n = len(P)
    if n < 3:
        yield {"points":P,"hull":P,"action":"done"}
        return

    hull = []
    l = 0
    for i in range(1, n):
        if P[i][0] < P[l][0]:
            l = i
    p = l

    while True:
        hull.append(P[p])
        q = (p + 1) % n
        yield {"points":P,"hull":hull.copy(),"current":P[p],"candidate":P[q],"action":"select_start"}
        for i in range(n):
            if i == p: continue
            yield {"points": P,"hull":hull.copy(),"current":P[p],"candidate":P[i],"action":"compare"}
            if orientation(P[p],P[i],P[q]) > 0:
                q = i
                yield {"points":P,"hull":hull.copy(),"current":P[p],"candidate":P[q],"action":"update_candidate"}
        p = q
        if p == l:
            break

    yield {"points":P,"hull":hull.copy(),"action":"done"}
