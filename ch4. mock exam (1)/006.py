import sys
input = sys.stdin.readline

N = int(input())

count_a = [0] * 100
count_b = [0] * 100

def calc_min_max_sum(count_a, count_b):
    max_sum = 0
    pos_a = 0
    pos_b = 99
    while pos_a < 100 and pos_b >= 0:
        if count_a[pos_a] > 0 and count_b[pos_b] > 0:
            max_sum = max(max_sum, pos_a + pos_b)
        if count_a[pos_a] <= count_b[pos_b]:
            count_b[pos_b] -= count_a[pos_a]
            pos_a += 1
        else:
            count_a[pos_a] -= count_b[pos_b]
            pos_b -= 1

    return max_sum

for _ in range(N):
    a, b = map(int, input().split())

    count_a[a] += 1
    count_b[b] += 1

    print(calc_min_max_sum(count_a[:], count_b[:]))
