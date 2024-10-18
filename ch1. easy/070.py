answer = [
    ['d', 'd', 'd'],
    ['d', 'c', 'b'],
    ['d', 'b', 'a'],
]


for _ in range(4):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())

    if x2 < x3 or x4 < x1:
        x_val = 0
    elif x2 == x3 or x1 == x4:
        x_val = 1
    else:
        x_val = 2

    if y2 < y3 or y4 < y1:
        y_val = 0
    elif y2 == y3 or y1 == y4:
        y_val = 1
    else:
        y_val = 2

    print(answer[x_val][y_val])