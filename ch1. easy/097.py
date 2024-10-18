G = int(input())

answer = []
for i in range(1, G + 1):
    if G % i == 0:
        j = G // i
        if j <= i:
            break

        if (j - i) % 2 == 0 and (j + i) % 2 == 0:
            a = (j - i) // 2
            b = (j + i) // 2
            answer.append(b)

if len(answer) == 0:
    print(-1)
else:
    answer.sort()
    for i in range(len(answer)):
        print(answer[i])