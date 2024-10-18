from collections import deque

A, B, C = map(int, input().split())
S = A + B + C

if S % 3 != 0:
    print(0)
else:
    visit = [[False] * S for _ in range(S)]
    queue = deque()

    queue.append((A, B))
    visit[A][B] = True

    while len(queue) != 0:
        a, b = queue.popleft()
        c = S - a - b

        D = [a, b, c]
        for i in range(3):
            x, y = D[i], D[(i + 1) % 3]
            if x == y:
                continue
            if x > y:
                x, y = y, x
            
            if not visit[x + x][y - x]:
                queue.append((x + x, y - x))
                visit[x + x][y - x] = True

    if visit[S // 3][S // 3]:
        print(1)
    else:
        print(0)