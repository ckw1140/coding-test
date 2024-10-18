N = int(input())

count = 1
while True:
    if N < count:
        if count % 2 == 1:
            print(count - N)
            break
        else:
            print(0)
            break

    N -= count
    count += 1