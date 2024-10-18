N = int(input())
A = list(map(int, input().split()))

count = 0
while True:
    if max(A) == 0:
        break

    found = False
    for i in range(N):
        if A[i] % 2 == 1:
            A[i] -= 1
            count += 1
            found = True

    if not found:
        for i in range(N):
            A[i] //= 2
        count += 1

print(count)