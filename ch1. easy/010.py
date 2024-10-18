N = int(input())

dp = [4] * (N + 1)

for i in range(1, N + 1):
    if i * i > N:
        break
    dp[i * i] = 1

for i in range(1, N + 1):
    if i * i > N:
        break

    for j in range(1, N + 1):
        if i * i + j * j > N:
            break
        
        if dp[i * i + j * j] != 1:
            dp[i * i + j * j] = 2


for i in range(1, N + 1):
    if dp[i] != 4:
        continue
    
    for j in range(1, N + 1):
        if j * j > N:
            break
        
        if dp[i - j * j] == 2:
            dp[i] = 3
            break

print(dp[N])