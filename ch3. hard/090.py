while True:
    N, A, B = map(int, input().split())
    if N == 0 and A == 0 and B == 0:
        break
    info = [list(map(int, input().split())) for _ in range(N)]

    sum_a = sum([info[i][0] for i in range(N)])
    dist = sum([info[i][0] * info[i][1] for i in range(N)])

    add = [(info[i][2] - info[i][1], info[i][0]) for i in range(N)]
    add.sort()

    sum_b = 0
    for i in range(N):
        if add[i][0] < 0:
            move = min(B - sum_b, add[i][1])
            sum_a -= move
            sum_b += move
            dist += move * add[i][0]
        elif sum_a > A:
            move = min(sum_a - A, add[i][1])
            sum_a -= move
            sum_b += move
            dist += move * add[i][0]

    print(dist)