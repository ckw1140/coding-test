N, M = map(int, input().split())
B = [input() for _ in range(N)]

min_x = 1e9
min_y = 1e9
max_x = 0
max_y = 0
for i in range(N):
    for j in range(M):
        if B[i][j] == '#':
            min_x = min(min_x, j)
            min_y = min(min_y, i)
            max_x = max(max_x, j)
            max_y = max(max_y, i)

center_x = (min_x + max_x) // 2
center_y = (min_y + max_y) // 2

if B[min_y][center_x] == '.':
    print("UP")
elif B[max_y][center_x] == '.':
    print("DOWN")
elif B[center_y][min_x] == '.':
    print("LEFT")
else:
    print("RIGHT")