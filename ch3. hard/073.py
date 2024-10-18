A, B, C, N = map(int, input().split())

found = False
for i in range(N // C + 1):
    for j in range((N - C * i) // B + 1):
        if (N - C * i - B * j) % A == 0:
            found = True
            break

if found:
    print(1)
else:
    print(0)