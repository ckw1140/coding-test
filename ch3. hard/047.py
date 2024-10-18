N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)

pair = []
pos = 0
while pos < N - 1:
    if A[pos] - A[pos + 1] <= 1:
        pair.append(A[pos + 1])
        pos += 2
    else:
        pos += 1

answer = 0
for i in range(0, len(pair) - 1, 2):
    answer += pair[i] * pair[i + 1]

print(answer)