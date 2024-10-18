from itertools import combinations

N = int(input())
S = list(map(int, input().split()))

sums = []
for i in range(1, N + 1):
    for combination in combinations(S, i):
        sums.append(sum(combination))

sums = list(set(sums))
sums.sort()

answer = len(sums) + 1
for i in range(len(sums)):
    if sums[i] != i + 1:
        answer = i + 1
        break

print(answer)