N = int(input())
A = list(map(int, input().split()))

for i in range(N):
    if i % 2 == 1:
        A[i] = 1 if A[i] == 0 else 0

group = []
count = 1
for i in range(1, N):
    if A[i] != A[i - 1]:
        group.append(count)
        count = 1
    else:
        count += 1

group.append(count)

answer = -1
for i in range(len(group)):
    answer = max(answer, group[i])
    if i + 1 < len(group):
        answer = max(answer, group[i] + group[i + 1])
    if i + 2 < len(group):
        answer = max(answer, group[i] + group[i + 1] + group[i + 2])

print(answer)