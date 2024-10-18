T = int(input())
mod = (10 ** 9) + 9

D = [0] * 100001
D[0] = 1
D[1] = 1
D[2] = 2
D[3] = 2
for i in range(4, 100001):
    D[i] += D[i - 2]
    if i >= 4:
        D[i] += D[i - 4]
    if i >= 6:
        D[i] += D[i - 6]

    D[i] %= mod

for _ in range(T):
    N = int(input())
    print(D[N])