N = int(input())

info = []
for i in range(N):
    x, y = map(int, input().split())
    info.append((x, y))

for i in range(N):
    count = 0
    for j in range(N):
        if i == j:
            continue

        if info[i][0] < info[j][0] and info[i][1] < info[j][1]:
            count += 1

    print(count + 1, end=" ")