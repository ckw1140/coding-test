N = int(input())
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())

min_time = 1e9
for i in range(N):
    if A[i] <= B[i]:
        min_time = min(min_time, B[i])

if min_time == 1e9:
    print(-1)
else:
    print(min_time)