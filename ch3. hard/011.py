N = int(input())
A = list(map(int, input().split()))

sqsum = sum(list(map(lambda x: x ** 2, A)))

print((sum(A) ** 2 - sqsum) // 2)