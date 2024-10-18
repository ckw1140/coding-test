N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
start = 0
end = N - 1

count = 0
while start < end:
    if A[start] + A[end] <= K:
        count += 1
        start += 1
        end -= 1
    else:
        end -= 1

print(count)