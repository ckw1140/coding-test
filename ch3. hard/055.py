N, B, A = map(int, input().split())
G = list(map(int, input().split()))
G.sort()

psum = [0] * N
psum[0] = G[0]
for i in range(1, N):
    psum[i] = psum[i - 1] + G[i]

answer = 0
for i in range(N):
    cost = psum[i] // 2
    if i + 1 > A:
        cost += psum[i - A] // 2

    if cost <= B:
        answer = i + 1

print(answer)