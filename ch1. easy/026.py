N, K = map(int, input().split())
A = list(map(int, input().split()))

count = [0] * 100001

start = 0
end = 0
count[A[start]] += 1


max_length = 0
good = True
while True:
    if good:
        max_length = max(max_length, end - start + 1)

        if end == N - 1:
            break
        
        end += 1
        count[A[end]] += 1
        if count[A[end]] == K + 1:
            good = False
    else:
        start += 1
        count[A[start - 1]] -= 1
        if count[A[start - 1]] == K:
            good = True

print(max_length)