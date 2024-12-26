L = int(input())
S = list(map(int, input().split()))
n = int(input())

if n in S:
    print(0)
else:
    S.sort()
    left = 0
    for i in range(L):
        if left < n and n < S[i]:
            print((n - left) * (S[i] - n) - 1)
            break
        left = S[i]
