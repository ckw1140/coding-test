N = int(input())
mod = 987654321

D = [0] * (N + 1)
D[0] = 1
for i in range(2, N + 1, 2):
    D[i] = 0
    for j in range(0, i - 1, 2):
        D[i] += D[j] * D[i - 2 - j] % mod
        D[i] %= mod

answer = 0
for i in range(0, N - 1, 2):
    answer += D[i] * D[N - 2 - i] % mod
    answer %= mod

print(answer)