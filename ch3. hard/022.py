N, M, K = map(int, input().split())
A = list(map(int, input().split()))

low, high = 0, N
p = -1

while low <= high:
    mid = (low + high) // 2

    count = 1
    la = A[0]
    for i in range(1, K):
        if A[i] - la >= mid:
            count += 1
            la = A[i]

    if count >= M:
        p = mid
        low = mid + 1
    else:
        high = mid - 1

answer = ['0'] * K
answer[0] = '1'
count = 1
la = A[0]
for i in range(1, K):
    if count == M:
        break
    if A[i] - la >= p:
        answer[i] = '1'
        count += 1
        la = A[i]

print("".join(answer))