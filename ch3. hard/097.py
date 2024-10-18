N = int(input())

def solve(n):
    fact = 1
    last = 1
    while n > 0:
        while n % (fact * (last + 1)) == 0:
            fact *= (last + 1)
            last += 1

        if n % fact == 0:
            n -= fact
            fact *= (last + 1)
            last += 1
        else:
            break

    return n == 0

if N != 0 and (solve(N) or solve(N - 1)):
    print("YES")
else:
    print("NO")