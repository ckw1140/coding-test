N, Q = map(int, input().split())
S = list(input())

for _ in range(Q):
    t, l, r = map(int, input().split())
    l -= 1
    r -= 1

    if t == 1:
        count = 0
        for i in range(l, r):
            if S[i] != S[i + 1]:
                count += 1

        print(count + 1)

    if t == 2:
        for i in range(l, r + 1):
            id = ord(S[i]) - ord('A')
            id = (id + 1) % 26
            S[i] = chr(id + ord('A'))