N, L = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]
state = ['R'] * N
remain = [info[i][1] for i in range(N)]

pos = 0
for i in range(10000):
    if pos == L:
        print(i)
        break
    
    stop = False
    for j in range(N):
        if info[j][0] == pos:
            if state[j] == 'R':
                stop = True
                break

    if not stop:
        pos += 1

    for j in range(N):
        remain[j] -= 1

        if remain[j] == 0:
            remain[j] = info[j][1] if state[j] == 'G' else info[j][2]
            state[j] = 'R' if state[j] == 'G' else 'G'

