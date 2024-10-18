N = int(input())

score = [0] * 3
count_3 = [0] * 3
count_2 = [0] * 3

for _ in range(N):
    s = list(map(int, input().split()))

    for i in range(3):
        score[i] += s[i]
        if s[i] == 3:
            count_3[i] += 1
        if s[i] == 2:
            count_2[i] += 1

max_score = 0
max_count_3 = 0
max_count_2 = 0
id = -1
for i in range(3):
    if max_score < score[i]:
        max_score = score[i]
        max_count_3 = count_3[i]
        max_count_2 = count_2[i]
        id = i
    elif max_score == score[i] and max_count_3 < count_3[i]:
        max_count_3 = count_3[i]
        max_count_2 = count_2[i]
        id = i
    elif max_score == score[i] and max_count_3 == count_3[i] and max_count_2 < count_2[i]:
        max_count_2 = count_2[i]
        id = i
    elif max_score == score[i] and max_count_3 == count_3[i] and max_count_2 == count_2[i]:
        id = -1
        
if id == -1:
    print(0, max_score)
else:
    print(id + 1, max_score)