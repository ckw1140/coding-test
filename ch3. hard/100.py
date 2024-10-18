N = int(input())
F = list(map(int, input().split()))

F.sort()

answer = 0
pos = 0
for i in range(N):
    while pos <= i and F[pos] * 10 < F[i] * 9:
        pos += 1

    answer += i - pos

print(answer)