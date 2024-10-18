N = int(input())

found = False
for i in range(3):
    if N // 5 < i:
        break

    a = (N // 5 - i)
    if (N - a * 5) % 3 == 0:
        b = (N - a * 5) // 3
        print(a + b)
        found = True
        break

if not found:
    print(-1)