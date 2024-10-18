S = input()
T = input()

D = [[False] * len(T) for _ in range(len(T))]
E = [[False] * len(T) for _ in range(len(T))]

# D[i][j], E[i][j]: i~j 길이 짧은거 부터
for i in range(0, len(T) - len(S) + 1):
    # i, i + len(S) - 1
    D[i][i + len(S) - 1] = T[i:i + len(S)] == S
    E[i][i + len(S) - 1] = T[i:i + len(S)][::-1] == S

for i in range(len(S) + 1, len(T) + 1):
    for j in range(0, len(T) - i + 1):
        # j~k, D[j][k], E[j][k]
        k = j + i - 1

        if T[k] == 'A':
            D[j][k] |= D[j][k - 1]
        if T[j] == 'B':
            D[j][k] |= E[j + 1][k]

        if T[j] == 'A':
            E[j][k] |= E[j + 1][k]
        if T[k] == 'B':
            E[j][k] |= D[j][k - 1]

if D[0][len(T) - 1]:
    print(1)
else:
    print(0)