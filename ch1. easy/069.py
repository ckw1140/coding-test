N, P = map(int, input().split())

order = {}
count = 0
n = N
while True:
    if n in order:
        print(count - order[n])
        break
    order[n] = count
    n = n * N % P
    count += 1