N, L, D = map(int, input().split())

check = [False] * 5000

index = 0
for i in range(N):
    for j in range(L):
        check[index] = True
        index += 1
    for j in range(5):
        index += 1

for i in range(0, 5000, D):
    if not check[i]:
        print(i)
        break