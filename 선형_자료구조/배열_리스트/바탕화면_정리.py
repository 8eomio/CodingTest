def solution(wallpaper):
    points = []
    for i, line in enumerate(wallpaper):
        for j, point in enumerate(line):
            if point == "#":
                points.append([i,j])
    minx,miny, maxx, maxy = points[0][1], points[0][0], points[0][1], points[0][0]

    for file in points:
        miny = min(file[0], miny)
        minx = min(file[1], minx)
        maxy = max(file[0]+1, maxy)
        maxx = max(file[1]+1, maxx)
    return [miny, minx, maxy, maxx]
