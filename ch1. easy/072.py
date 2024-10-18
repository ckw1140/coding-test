N = int(input())
X = [0] * N

for i in range(N):
    X[i] = int(input())


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    else:
        return gcd(b,  a % b)


d = 0
for i in range(N - 1):
    d = gcd(d, X[i + 1] - X[i])

print((X[-1] - X[0]) // d + 1 - N)