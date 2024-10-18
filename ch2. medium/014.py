N = int(input())
A = list(map(int, input().split()))

A.sort()
count = 0
for i in range(N):
    pos = N - 1
    if pos == i:
        pos -= 1
    
    found = False
    for j in range(N):
        if i == j:
            continue

        target = A[i] - A[j]

        while pos > j and A[pos] > target:
            pos -= 1
            if pos == i:
                pos -= 1

        if j != pos and A[pos] == target:
            found = True
            break

    if found:
        count += 1

print(count)