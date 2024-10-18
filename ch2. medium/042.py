N = int(input())
M = int(input())
C = list(map(int, input().split()))

count = [0] * 100
last = [-1] * 100

for i in range(M):
    C[i] -= 1

    # 추천
    count[C[i]] += 1

    if last[C[i]] != -1:
        continue

    picture = 0
    for j in range(100):
        if last[j] != -1:
            picture += 1

    if picture == N:
        # 탈락
        min_count = 1e9
        min_last = 1e9
        who = -1
        for j in range(100):
            if last[j] == -1:
                continue
            if min_count > count[j]:
                min_count = count[j]
                min_last = last[j]
                who = j
            elif min_count == count[j] and min_last > last[j]:
                min_last = last[j]
                who = j

        count[who] = 0
        last[who] = -1

    # 추가
    last[C[i]] = i

for i in range(100):
    if last[i] != -1:
        print(i + 1, end=" ")