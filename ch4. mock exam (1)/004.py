while True:
    N = int(input())
    if N == 0:
        break

    answer = 0
    for i in range(N):
        for j in range(N):
            answer += min(N - i, N - j)

    print(answer)
