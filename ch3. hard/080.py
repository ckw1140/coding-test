N = int(input())
A = [int(input()) for _ in range(N)]

left = [-1] * N
right = [N] * N

stack = []
for i in range(N):
    while len(stack) > 0 and A[stack[-1]] <= A[i]:
        stack.pop(-1)

    if len(stack) > 0:
        left[i] = stack[-1]

    stack.append(i)

stack = []
for i in range(N - 1, -1, -1):
    while len(stack) > 0 and A[stack[-1]] < A[i]:
        stack.pop(-1)

    if len(stack) > 0:
        right[i] = stack[-1]

    stack.append(i)

answer = 0
for i in range(N):
    if left[i] == -1 and right[i] == N:
        continue

    left_value = A[left[i]] if left[i] != -1 else 1e12
    right_value = A[right[i]] if right[i] != N else 1e12

    answer += min(left_value, right_value) - A[i]

print(answer)