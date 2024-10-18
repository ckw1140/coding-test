from queue import PriorityQueue

N = int(input())
A = list(map(int, input().split()))

pq = PriorityQueue()
for i in range(N):
    pq.put(-A[i])

count = 0
while pq.qsize() >= 2:
    x = -pq.get()
    y = -pq.get()
    
    x -= 1
    y -= 1
    if x > 0:
        pq.put(-x)
    if y > 0:
        pq.put(-y)
    
    count += 1

if pq.qsize() > 0:
    count += -pq.get()

if count > 60 * 24:
    print(-1)
else:
    print(count)