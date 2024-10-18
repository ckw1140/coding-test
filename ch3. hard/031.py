N = int(input())
A = list(map(int, input().split()))

def shift(a, k):
    return a[k:] + a[:k]

def is_ascending(a):
    for i in range(1, len(a)):
        if a[i - 1] > a[i]:
            return False
    return True

def is_descending(a):
    for i in range(1, len(a)):
        if a[i - 1] < a[i]:
            return False
    return True


answer = 1e9
max_idx = A.index(max(A))
if is_descending(shift(A, max_idx)):
    answer = min(answer, max_idx)

min_idx = A.index(min(A))
if is_ascending(shift(A, min_idx)):
    answer = min(answer, min_idx)

if answer == 1e9:
    print(-1)
else:
    print(answer)