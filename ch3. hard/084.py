N, X = map(int, input().split())

if N <= X and X <= 26 * N:
    answer = []
    for i in range(N):
        n = N - 1 - i

        if X - 1 - 26 * n < 0:
            answer.append('A')
            X -= 1
        else:
            answer.append(chr(ord('A') + X - 1 - 26 * n))
            X -= ord(answer[-1]) - ord('A') + 1

    print("".join(answer))
else:
    print("!")