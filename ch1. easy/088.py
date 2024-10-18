N = int(input())

D = [0] * (N + 1)

for i in range(1, N + 1):
    if (i ** 0.5).is_integer():
        D[i] = 1
        continue
    
    D[i] = 1e9

    a = 1
    while a * a <= i / 2:
        D[i] = min(D[i], 1 + D[i - a * a])
        a += 1

print(D[N])