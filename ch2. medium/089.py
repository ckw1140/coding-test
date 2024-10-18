from collections import deque

S = input()

queue = deque()
for i in range(len(S)):
    if S[i] == 'B':
        queue.append(i)

answer = 0
for i in range(len(S)):
    if S[i] == 'C':
        if len(queue) != 0 and queue[0] < i:
            queue.popleft()
            answer += 1

for i in range(len(S) - 1, -1, -1):
    if S[i] == 'A':
        if len(queue) != 0 and queue[-1] > i:
            queue.pop()
            answer += 1

print(answer)