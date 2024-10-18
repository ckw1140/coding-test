T = int(input())

for _ in range(T):
    S = input().split()

    for v in S:
        print(v[::-1], end=" ")
    print()