A, B, C = map(int, input().split())

def power(a, b, c):
    if b == 1:
        return a % c
    x = power(a, b // 2, C) ** 2 % c
    if b % 2 == 1:
        return x * a % c
    else:
        return x

print(power(A, B, C))