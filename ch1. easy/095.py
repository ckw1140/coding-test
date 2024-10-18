from itertools import combinations

N = int(input())

A = []
for i in range(1, 7):
    for j in range(i + 1):
        for combination in combinations(range(i), j):
            number = 0
            for k in range(i):
                number *= 10
                if k in combination:
                    number += 7
                else:
                    number += 4

            A.append(number)


max_val = -1
for i in range(len(A)):
    if A[i] <= N:
        max_val = max(max_val, A[i])

print(max_val)