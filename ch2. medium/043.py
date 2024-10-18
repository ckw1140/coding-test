A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

if A < 0 and B < 0:
    print((B - A) * C)
elif A < 0 and 0 < B:
    print(-A * C + D + B * E)
else:
    print((B - A) * E)