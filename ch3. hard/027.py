import sys
input = sys.stdin.readline

N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]

red = []
blue = []
for i in range(N):
    if (P[i][0] + P[i][1]) % 2 == 0:
        red.append(i + 1)
    else:
        blue.append(i + 1)

if len(red) == 0 or len(blue) == 0:
    print("NO")
else:
    print("YES")
    print(*(red + blue))