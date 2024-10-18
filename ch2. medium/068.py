N = int(input())

num_2s = 0
num_5s = 0
for i in range(1, N + 1):
    n = i
    while n % 2 == 0:
        n /= 2
        num_2s += 1
    while n % 5 == 0:
        n /= 5
        num_5s += 1

print(min(num_2s, num_5s))