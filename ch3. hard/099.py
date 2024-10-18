N = int(input())
A, B = map(int, input().split())
C = int(input())
D = [int(input()) for _ in range(N)]

D.sort(reverse=True)

answer = C // A
for i in range(N):
    C += D[i]
    answer = max(answer, C // (A + B * (i + 1)))

print(answer)