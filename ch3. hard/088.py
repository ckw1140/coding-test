N, M, K = map(int, input().split())
B = [input() for _ in range(N)]

num_changes = 0
tiles = [[] for _ in range(K)]
for i in range(K):
    for j in range(K):
        count = {}
        for a in range(N // K):
            for b in range(M // K):
                x = B[a * K + i][b * K + j]
                if x not in count:
                    count[x] = 0
                count[x] += 1

        max_key = max(count, key=count.get)
        num_changes += N // K * M // K - count[max_key]
        tiles[i].append(max_key)

print(num_changes)

for i in range(N // K):
    for j in range(K):
        print("".join(tiles[j]) * (M // K))