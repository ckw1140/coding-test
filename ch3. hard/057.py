N, K = map(int, input().split())
A = list(map(int, input().split()))
A = [A[i] - K for i in range(N)]

psum = [0] * N
psum[0] = A[0]
for i in range(1, N):
    psum[i] = psum[i - 1] + A[i]

answer = 0
count = {}
count[0] = 1
for i in range(N):
    if psum[i] not in count:
        count[psum[i]] = 0
    answer += count[psum[i]]
    count[psum[i]] += 1

print(answer)