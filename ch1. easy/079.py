from itertools import combinations

A = [int(input()) for _ in range(9)]

for combination in combinations(A, 7):
    if sum(combination) == 100:
        for i in combination:
            print(i)
        break