from queue import PriorityQueue

N = int(input())
R = [list(map(int, input().split())) for _ in range(N)]
D = int(input())

pq = PriorityQueue()
num_cands = 0
for i in range(N):
    if R[i][0] > R[i][1]:
        R[i][0], R[i][1] = R[i][1], R[i][0]
    if R[i][1] - R[i][0] > D:
        continue
    pq.put(R[i][1])
    num_cands += 1

R.sort()
answer = 0
left = 0
for i in range(N):
    if R[i][1] - R[i][0] > D:
        continue
    while pq.qsize() != 0:
        x = pq.get()
        if x > R[i][0] + D:
            pq.put(x)
            break

    answer = max(answer, num_cands - left - pq.qsize())
    left += 1

print(answer)