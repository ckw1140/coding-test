import sys
input = sys.stdin.readline

N = int(input())
B = [int(input()) for _ in range(N)]
B.sort()

answer = 0
max_val = 0
for i in range(N - 1, -1, -1):
    if B[i] + N >= max_val:
        answer += 1
    else:
        break

    max_val = max(max_val, B[i] + N - i)

print(answer)