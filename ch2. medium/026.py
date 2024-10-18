N = int(input())

D = [False] * (1001)
D[0] = False
D[1] = True
D[2] = False
D[3] = True
D[4] = True
for i in range(5, N + 1):
    D[i] = (not D[i - 1]) | (not D[i - 3]) | (not D[i - 4])

if D[N]:
    print("SK")
else:
    print("CY")