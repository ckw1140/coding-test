from queue import PriorityQueue

N = int(input())

courses = []

for _ in range(N):
    start, end = map(int, input().split())
    courses.append((start, end))

courses.sort()

pq = PriorityQueue()
pq.put(courses[0][1])
count = 1

for i in range(1, N):
    earliest = pq.get()
    if earliest <= courses[i][0]:
        pq.put(courses[i][1])
    else:
        pq.put(earliest)
        pq.put(courses[i][1])
        count += 1

print(count)