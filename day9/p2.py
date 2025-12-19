from collections import defaultdict
from itertools import combinations

if __name__ == "__main__":
    #points = [(1,2),(1,4),(4,4), (4,1), (2,1), (2,2)] # (x,y)
    with open("input.txt", "r") as f: 
            data = f.readlines()
            points = [[int(a) for a in line.strip().split(',')] for line in data]

    def _crossings(points):
        vertical = defaultdict(list)
        n = len(points)
        for k in range(n):
            a, b = points[k], points[(k+1) % n]
            if a[0] == b[0]:
                for y in range(min(a[1], b[1]), max(a[1], b[1])):
                    vertical[y].append(a[0])
        for y in vertical.keys():
            vertical[y].sort()
        return vertical
    vertical = _crossings(points)

    boundary = set() 
    n = len(points)
    for k in range(n):
        a, b = points[k], points[(k+1) % n]
        
        minx, maxx = min(a[0], b[0]), max(a[0], b[0])
        miny, maxy = min(a[1], b[1]), max(a[1], b[1])

        for x in range(minx, maxx+1):
            for y in range(miny, maxy+1):
                boundary.add((x,y))

    def _area(pair):
        a, b = pair
        minx, maxx = min(a[0], b[0]), max(a[0], b[0])
        miny, maxy = min(a[1], b[1]), max(a[1], b[1])

        return ((maxx-minx+1)*(maxy-miny+1))

    decreasing_rectangles = sorted(combinations(points, 2), key=_area, reverse=True)

    max_area = 0 
    rectangle = []

    for a, b in decreasing_rectangles: # Does the interior contain another point? 
        minx, maxx = min(a[0], b[0]), max(a[0], b[0])
        miny, maxy = min(a[1], b[1]), max(a[1], b[1])

        # Check if at least one point in the bulk is inside: 
        test_point = (minx+1, miny+1)
        crossings = vertical[miny+1]
        if sum([1 for c in crossings if c > minx+1])%2 == 0:
            continue # point is outside

        # Check for boundary points? 
        interior_points = False
        for point in boundary:
            if minx < point[0] < maxx and miny < point[1] < maxy: 
                interior_points = True
                break

        if interior_points:
            continue
        
        max_area = (maxx-minx+1)*(maxy-miny+1)
        rectangle = ((minx, miny), (maxx,maxy))
        break

    print(max_area, rectangle) # should be good