from queue import PriorityQueue

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
D = [False] * 1000001

pq = PriorityQueue()
for i in range(N):
    pq.put((-W[i][1] + 1, W[i][0]))

answer = -1
for i in range(1000000, -1, -1):
    if D[i]:
        continue
    
    x = pq.get()

    deadline = -x[0]
    if deadline >= i and i - x[1] + 1 >= 0:
        for j in range(i - x[1] + 1, i + 1):
            D[j] = True
    else:
        pq.put(x)

    if pq.qsize() == 0:
        answer = i - x[1] + 1
        break

print(answer)