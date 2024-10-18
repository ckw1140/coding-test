S = input()
A = list(map(int, list(S)))

psum = [0] * len(A)
psum[0] = A[0]
for i in range(1, len(A)):
    psum[i] = psum[i - 1] + A[i]


def range_sum(l, r):
    ret = psum[r]
    if l > 0:
        ret -= psum[l - 1]
    return ret

answer = 0
for i in range(2, len(A) + 1, 2):
    for j in range(len(A) - i + 1):
        left = range_sum(j, j + i // 2 - 1)
        right = range_sum(j + i // 2, j + i - 1)
        if left == right:
            answer = i

print(answer)