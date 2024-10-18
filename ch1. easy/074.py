N = int(input())
A = list(map(int, input().split()))

max_count = 1
count = 1
for i in range(1, N):
    if A[i - 1] <= A[i]:
        count += 1
    else:
        count = 1
    max_count = max(max_count, count)


A = A[::-1]
count = 1
for i in range(1, N):
    if A[i - 1] <= A[i]:
        count += 1
    else:
        count = 1
    max_count = max(max_count, count)


print(max_count)