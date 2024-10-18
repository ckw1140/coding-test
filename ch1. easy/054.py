N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

count = {}
for i in range(N):
    if A[i] not in count:
        count[A[i]] = [0, 0]
    count[A[i]][0] += 1
for i in range(N):
    if B[i] not in count:
        count[B[i]] = [0, 0]
    count[B[i]][1] += 1

answer = 0
for key, value in count.items():
    supply = value[0]
    demand = value[1]

    answer += min(supply, demand)

print(N - answer)