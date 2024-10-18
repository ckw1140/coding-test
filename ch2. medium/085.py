M, N = map(int, input().split())
A = [int(input()) for _ in range(N)]
mod = 2 ** 64

debt = max(0, sum(A) - M)

low, high, p = 0, max(A), -1

while low <= high:
    mid = (low + high) // 2

    pay_back = 0
    for i in range(N):
        if A[i] >= mid:
            pay_back += mid
        else:
            pay_back += A[i]

    if debt <= pay_back:
        p = mid
        high = mid - 1
    else:
        low = mid + 1


# p, p - 1, A[i]

angry = [0] * N
for i in range(N):
    if A[i] >= p - 1:
        debt -= p - 1
        angry[i] += p - 1
        A[i] -= p - 1
    else:
        debt -= A[i]
        angry[i] += A[i]
        A[i] = 0

if debt:
    for i in range(N):
        if debt > 0 and A[i] > 0:
            debt -= 1
            angry[i] += 1
            A[i] -= 1

answer = 0
for i in range(N):
    answer += (angry[i] ** 2) % mod
    answer %= mod

print(answer)