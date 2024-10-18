N, X = map(int, input().split())
S = [0] * N
T = [0] * N

for i in range(N):
    S[i], T[i] = map(int, input().split())

max_time = 0
for i in range(N):
    if S[i] + T[i] <= X:
        max_time = max(max_time, S[i])

if max_time == 0:
    print(-1)
else:
    print(max_time)