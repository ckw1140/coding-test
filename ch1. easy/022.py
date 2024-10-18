N, K = map(int, input().split())
A = list(map(int, input().split()))

psum = [0] * N
psum[0] = A[0]
for i in range(1, N):
    psum[i] = psum[i - 1] + A[i]

answer = 0
count = {}
for i in range(N):
    goal = psum[i] - K
    if goal == 0:
        answer += 1
    if goal in count:
        answer += count[goal]
    
    if psum[i] not in count:
        count[psum[i]] = 0
    count[psum[i]] += 1

print(answer)