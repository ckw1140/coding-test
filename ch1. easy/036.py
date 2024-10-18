N = int(input())
K = int(input())


low = 1
high = N * N
answer = -1

while low <= high:
    mid = (low + high) // 2

    count = 0
    for i in range(1, N + 1):
        count += min(N, (mid - 1) // i)

    if count < K:
        answer = mid
        low = mid + 1
    else:
        high = mid - 1

print(answer)