import sys
input = sys.stdin.readline

N = int(input())
H = [0] * N

for i in range(N):
    H[i] = int(input())

max_height = 0
count = 0
for i in range(N - 1, -1, -1):
    if max_height < H[i]:
        max_height = H[i]
        count += 1

print(count)