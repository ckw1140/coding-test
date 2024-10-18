S1, S2, S3 = map(int, input().split())

count = [0] * (S1 + S2 + S3 + 1)

for i in range(1, S1 + 1):
    for j in range(1, S2 + 1):
        for k in range(1, S3 + 1):
            count[i + j + k] += 1

max_val = -1
who = -1
for i in range(1, S1 + S2 + S3 + 1):
    if max_val < count[i]:
        max_val = count[i]
        who = i

print(who)