N = int(input())
A = list(map(int, input().split()))

psum = [0] * N
psum[0] = A[0]
for i in range(1, N):
    psum[i] = psum[i - 1] + A[i]

left = [-1] * N
right = [N] * N

stack = []
for i in range(N):
    while len(stack) != 0 and stack[-1][0] >= A[i]:
        stack.pop(-1)

    if len(stack) != 0:
        left[i] = stack[-1][1]

    stack.append((A[i], i))

stack = []
for i in range(N - 1, -1, -1):
    while len(stack) != 0 and stack[-1][0] >= A[i]:
        stack.pop(-1)

    if len(stack) != 0:
        right[i] = stack[-1][1]

    stack.append((A[i], i))

max_score = -1
start, end = -1, N
for i in range(N):
    range_sum = psum[right[i] - 1]
    if left[i] != -1:
        range_sum -= psum[left[i]]
    score = A[i] * range_sum
    if max_score < score:
        max_score = score
        start = left[i] + 1
        end = right[i] - 1

print(max_score)
print(start + 1, end + 1)