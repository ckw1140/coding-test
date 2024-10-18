N = int(input())
V = [list(map(int, input().split())) for _ in range(N)]

V.sort()

psum1 = [0] * N
psum2 = [0] * N

psum1[0] = V[0][1]
psum2[0] = V[0][0] * V[0][1]

for i in range(1, N):
    psum1[i] = psum1[i - 1] + V[i][1]
    psum2[i] = psum2[i - 1] + V[i][0] * V[i][1]


min_dist = 1e25
answer = -1
for i in range(N):
    left = 0
    right = 0

    if i > 0:
        left += psum1[i - 1] * V[i][0]
        left -= psum2[i - 1]

    right += psum2[N - 1] - psum2[i]
    right -= (psum1[N - 1] - psum1[i]) * V[i][0]

    if min_dist > left + right:
        min_dist = left + right
        answer = V[i][0]

print(answer)