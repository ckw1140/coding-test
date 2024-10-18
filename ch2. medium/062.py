import sys

input = sys.stdin.readline

N = int(input())

bude = set()

count = 0
for _ in range(N):
    a, b = map(int, input().split())

    if b == 1:
        if a in bude:
            count += 1
        else:
            bude.add(a)
    if b == 0:
        if a not in bude:
            count += 1
        else:
            bude.remove(a)

count += len(bude)

print(count)