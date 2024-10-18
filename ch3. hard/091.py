N = int(input())

count = [0] * 10
leading = [False] * 10

for _ in range(N):
    S = input()

    for i in range(len(S)):
        count[ord(S[i]) - ord('A')] += 10 ** (len(S) - i - 1)

    leading[ord(S[0]) - ord('A')] = True

answer = 0
for i in range(10):
    # i번째 알파벳이 0인 경우
    if leading[i]:
        continue

    remain = []
    for j in range(10):
        if j == i:
            continue

        remain.append(count[j])

    remain.sort(reverse=True)
    result = 0
    for j in range(len(remain)):
        result += (9 - j) * remain[j]

    answer = max(answer, result)

print(answer)