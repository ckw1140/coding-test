from itertools import permutations

X = []
Y = []
for _ in range(4):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)


min_move = 1e9
for permutation in permutations([1, 2, 3], 3):
    x = X[0]
    y = Y[0]
    move = 0
    for i in permutation:
        move += (abs(x - X[i]) ** 2 + abs(y - Y[i]) ** 2) ** 0.5
        x = X[i]
        y = Y[i]

    min_move = min(min_move, int(move))

print(min_move)