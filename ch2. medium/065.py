from itertools import combinations

T = int(input())

D = [0] * 50
D[0] = 1
for i in range(1, 50):
    D[i] = D[i - 1] + i + 1

E = [[False] * 4 for _ in range(1001)]
E[0][0] = True
for i in range(1, 1001):
    for j in range(1, 4):
        E[i][j] = False

        for k in D:
            if i < k:
                break
            E[i][j] |= E[i - k][j - 1]

for _ in range(T):
    N = int(input())

    if E[N][3]:
        print("1")
    else:
        print("0")