N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)

if A[0] < B[0]:
    print(-1)
else:
    count = 0
    while len(B) > 0:
        for a in A:
            if len(B) > 0 and a < B[-1]:
                break
            for b in B:
                if b <= a:
                    B.remove(b)
                    break
        count += 1

    print(count)