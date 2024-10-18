N = int(input())
A = [int(input()) for _ in range(N)]
A.sort()

check = set()
for i in range(N):
    for j in range(i, N):
        check.add(A[i] + A[j])

for i in range(N):
    for j in range(i):
        if A[i] - A[j] in check:
            answer = A[i]

print(answer)