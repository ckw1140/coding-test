d, k = map(int, input().split())

D = [0] * (d + 1)
E = [0] * (d + 1)

D[1] = 1
E[1] = 0
D[2] = 0
E[2] = 1
for i in range(3, d + 1):
    D[i] = D[i - 1] + D[i - 2]
    E[i] = E[i - 1] + E[i - 2]

for A in range(1, k // D[d] + 1):
    if (k - A * D[d]) % E[d] == 0:
        print(A)
        print((k - A * D[d]) // E[d])
        break