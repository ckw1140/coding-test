from collections import deque

A, B, C = map(int, input().split())
S = [A, B, C]

visit = set()
queue = deque()
queue.append((0, 0, C))
visit.add((0, 0, C))
answer = []

while len(queue) != 0:
    a, b, c = queue.popleft()
    
    if a == 0:
        answer.append(c)

    for i in range(3):
        for j in range(3):
            if i == j:
                continue

            s = [a, b, c]

            # i -> j
            if s[i] + s[j] <= S[j]:
                s[j] += s[i]
                s[i] = 0
            else:
                s[i] = s[i] + s[j] - S[j]
                s[j] = S[j]

            if (s[0], s[1], s[2]) not in visit:
                queue.append((s[0], s[1], s[2]))
                visit.add((s[0], s[1], s[2]))

answer = list(set(answer))
answer.sort()
print(*answer)