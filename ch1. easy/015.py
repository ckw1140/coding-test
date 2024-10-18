from itertools import combinations

L, C = map(int, input().split())
A = input().split()

A.sort()

for combination in combinations(A, L):
    moum = 0
    jaum = 0
    for a in combination:
        if a in {'a', 'e', 'i', 'o', 'u'}:
            moum += 1
        else:
            jaum += 1
    if moum >= 1 and jaum >= 2:
        print("".join(combination))