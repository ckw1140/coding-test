S = input()

D = [0] * (len(S) + 1)
D[0] = 1

for i in range(1, len(S) + 1):
    D[i] = 0
    if S[i - 1] != '0':
        D[i] = D[i - 1]
    if i >= 2 and S[i - 2] != '0' and int(S[i - 2:i]) <= 34:
        D[i] += D[i - 2]

print(D[len(S)])