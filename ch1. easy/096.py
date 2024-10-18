N = int(input())

mod = 15746

D = [0] * 1000001
D[1] = 1
D[2] = 2
for i in range(3, N + 1):
    D[i] = D[i - 1] + D[i - 2]
    D[i] %= mod

print(D[N])