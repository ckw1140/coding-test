N = int(input())
M = int(input())

if N > M:
    print(0)
else:
    # M - 1, M - N

    answer = 1
    for i in range(1, M - N + 1):
        answer *= (M - i)
        answer //= i

    print(answer)