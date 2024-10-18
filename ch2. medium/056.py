import sys
from queue import PriorityQueue

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    Q = int(input())

    min_pq = PriorityQueue()
    max_pq = PriorityQueue()
    count = {}

    for _ in range(Q):
        t, v = input().split()
        v = int(v)

        if t == "I":
            min_pq.put(v)
            max_pq.put(-v)
            if v not in count:
                count[v] = 0
            count[v] += 1
        if t == "D":
            if v == 1:
                while max_pq.qsize() != 0:
                    x = -max_pq.get()
                    if count[x] != 0:
                        count[x] -= 1
                        break
            if v == -1:
                while min_pq.qsize() != 0:
                    x = min_pq.get()
                    if count[x] != 0:
                        count[x] -= 1
                        break

    max_val = -1e12
    while max_pq.qsize() != 0:
        x = -max_pq.get()
        if count[x] != 0:
            max_val = x
            break

    min_val = 1e12
    while min_pq.qsize() != 0:
        x = min_pq.get()
        if count[x] != 0:
            min_val = x
            break

    if max_val == -1e12:
        print("EMPTY")
    else:
        print(max_val, min_val)