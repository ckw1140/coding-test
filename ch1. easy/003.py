N = int(input())

found = False
for i in range(N // 2 + 1):
  if (N - 2 * i) % 5 == 0:
    print(i + (N - 2 * i) // 5)
    found = True
    break

if not found:
  print(-1)