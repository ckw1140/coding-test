H, W = map(int, input().split())
A = list(map(int, input().split()))

B = [[0] * W for _ in range(H)]

for i in range(W):
    for j in range(A[i]):
        B[H - 1 - j][i] = 1

count = 0
for i in range(H):
    for j in range(W):
        if B[i][j] == 1:
            continue

        k = j
        while k >= 0:
            if B[i][k] == 1:
                break
            k -= 1
        
        if k == -1:
            continue

        k = j
        while k < W:
            if B[i][k] == 1:
                break
            k += 1
        
        if k == W:
            continue
        
        count += 1

print(count)