N = int(input())

count = 0
for _ in range(N):
    S = input()

    good = True
    for a in range(26):
        indices = []
        for i in range(len(S)):
            if ord(S[i]) - ord('a') == a:
                indices.append(i)
        
        for i in range(len(indices) - 1):
            if indices[i] + 1 != indices[i + 1]:
                good = False
                break

        if not good:
            break

    if good:
        count += 1

print(count)