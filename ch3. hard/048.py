N = int(input())
A = list(map(int, input().split()))

B = [0] * (N + 1)
for i in range(N):
    B[A[i]] = i

C = [0] * N
pos = N
while pos > 0:
    if pos > 1 and B[pos] < B[pos - 1]:
        C[B[pos]] = pos - 1
        C[B[pos - 1]] = pos
        pos -= 2
    else:
        C[B[pos]] = pos
        pos -= 1

print(*C)