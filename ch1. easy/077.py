N, M = map(int, input().split())
B = [input() for _ in range(N)]

for i in range(N):
    print(B[i][::-1])