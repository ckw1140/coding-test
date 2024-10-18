A, B, C = map(int, input().split())
D = int(input())

for _ in range(D):
    C += 1
    if C == 60:
        B += 1
        C = 0
    if B == 60:
        A += 1
        B = 0
    if A == 24:
        A = 0

print(A, B, C)