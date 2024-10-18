from collections import deque

N = int(input())

queue = deque()

for i in range(1, N + 1):
    queue.append(i)

while len(queue) != 1:
    n = len(queue)

    for i in range(n):
        if i % 2 == 0:
            queue.popleft()
        else:
            queue.append(queue.popleft())

print(queue[0])