N = int(input())
A = list(map(int, input().split()))
A = [A[i] - 1 for i in range(N)]

def is_sorted(a):
    for i in range(N):
        if a[i] != i:
            return False
    return True

def reverse(a, l, r):
    return a[:l] + a[l:r + 1][::-1] + a[r + 1:]

def one_reverse(a):
    moved = []
    for i in range(N):
        if a[i] != i:
            moved.append(i)

    if len(moved) == 0:
        return [1, 1]
    else:
        l = moved[0]
        r = moved[-1]

        if is_sorted(reverse(a, l, r)):
            return [l, r]
        else:
            return [-1, -1]


moved = []
for i in range(N):
    if A[i] != i:
        moved.append(i)

min_val, min_pos = 1e9, -1
max_val, max_pos = -1e9, -1
for i in range(len(moved)):
    if min_val > A[moved[i]]:
        min_val = A[moved[i]]
        min_pos = moved[i]
    if max_val < A[moved[i]]:
        max_val = A[moved[i]]
        max_pos = moved[i]

answer = []
if min_pos != -1:
    res = one_reverse(reverse(A, min_val, min_pos))
    if res != [-1, -1]:
        answer = [[min_val, min_pos], res]

if max_pos != -1:
    res = one_reverse(reverse(A, max_pos, max_val))
    if res != [-1, -1]:
        answer = [[max_pos, max_val], res]

while len(answer) < 2:
    answer.append([0, 0])

for l, r in answer:
    print(l + 1, r + 1)