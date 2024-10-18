N = int(input())
W = [0] * N

for i in range(N):
    W[i] = int(input())

W.sort(reverse=True)

max_weight = 0
for i in range(N):
    max_weight = max(max_weight, W[i] * (i + 1))

print(max_weight)