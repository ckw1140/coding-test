N = int(input())
H = [list(map(int, input().split())) for _ in range(N)]

H.sort(key=lambda x: x[1], reverse=True)

S = [False] * 1001

answer = 0
for i in range(N):
    for j in range(H[i][0], 0, -1):
        if not S[j]:
            S[j] = True
            answer += H[i][1]
            break

print(answer)