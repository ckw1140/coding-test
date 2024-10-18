N = int(input())
X = list(map(int, input().split()))

X.sort()
psum = [0] * N
psum[0] = X[0]
for i in range(1, N):
    psum[i] = psum[i - 1] + X[i]


answer = 0
for i in range(N):
    if i > 0:
        answer += X[i] * i - psum[i - 1]
    if i < N - 1:
        answer += psum[N - 1] - psum[i] - X[i] * (N - 1 - i)

print(answer)