T = int(input())

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for _ in range(T):
    S = input()

    did = 1
    x = 0
    y = 0

    minx = 0
    miny = 0
    maxx = 0
    maxy = 0
    for s in S:
        if s == 'F':
            x += directions[did][0]
            y += directions[did][1]
        if s == 'B':
            x -= directions[did][0]
            y -= directions[did][1]
        if s == 'L':
            did = (did + 1) % 4
        if s == 'R':
            did = (did + 3) % 4

        minx = min(minx, x)
        miny = min(miny, y)
        maxx = max(maxx, x)
        maxy = max(maxy, y)

    print((maxx - minx) * (maxy - miny))
