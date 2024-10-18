from collections import deque

N, K = map(int, input().split())

queue = deque()

for i in range(K, N + 1):
    queue.append(i)
for i in range(1, K):
    queue.append(i)


answer = []
while True:
    answer.append(queue.popleft())
    
    if len(queue) == 0:
        break
    
    for _ in range(K - 1):
        queue.append(queue.popleft())
    
print("<", end="")
for i in range(N - 1):
    print(answer[i], end=", ")
print(answer[N - 1], end=">")