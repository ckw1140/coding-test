S = input()
N = int(input())
A = [input() for _ in range(N)]

D = [False] * (len(S))

for i in range(len(S)):
    for a in A:
        if len(a) <= i + 1 and S[i - len(a) + 1:i + 1] == a:
            if len(a) == i + 1:
                D[i] = True
            else:
                D[i] |= D[i - len(a)]

if D[-1]:
    print(1)
else:
    print(0)