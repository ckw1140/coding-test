N, X = map(int, input().split())

D = []
score = 0
for _ in range(N):
    b, a = map(int, input().split())

    X -= 1000
    D.append(b - a)
    score += a

D.sort(reverse=True)
for i in range(N):
    if X >= 4000 and D[i] > 0:
        X -= 4000
        score += D[i]

print(score)