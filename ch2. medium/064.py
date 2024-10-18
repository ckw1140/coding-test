from itertools import combinations

T = int(input())

D = [0] * 50
D[0] = 1
for i in range(1, 50):
    D[i] = D[i - 1] + i + 1

for _ in range(T):
    N = int(input())

    found = False
    for combination in combinations(D, 3):
        if sum(combination) == N:
            found = True
            break

    for combination in combinations(D, 2):
        if 2 * combination[0] + combination[1] == N:
            found = True
            break
        if combination[0] + 2 * combination[1] == N:
            found = True
            break
    
    if N % 3 == 0 and N / 3 in D:
        found = True

    if found:
        print("1")
    else:
        print("0")