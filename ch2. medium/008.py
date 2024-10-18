N = int(input())
A = list(map(int, input().split()))
X = int(input())

count = [0] * 1000001
for i in range(N):
    count[A[i]] += 1

answer = 0
for i in range((X + 1) // 2):
    if X - i >= 1000000:
        continue
    answer += count[i] * count[X - i]

if X % 2 == 0:
    answer += count[X // 2] * (count[X // 2] - 1) // 2

print(answer)