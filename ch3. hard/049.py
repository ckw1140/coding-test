import sys

input = sys.stdin.readline


N = int(input())
A = [int(input()) for _ in range(N)]
psum = [0] * N
psum[0] = A[0]
for i in range(1, N):
    psum[i] = psum[i - 1] + A[i]

stack = []
left = [-1] * N
for i in range(N):
    while len(stack) != 0 and stack[-1][0] < A[i]:
        stack.pop(-1)

    if len(stack) != 0:
        left[i] = stack[-1][1]

    stack.append((A[i], i))

stack = []
right = [N] * N
for i in range(N - 1, -1, -1):
    while len(stack) != 0 and stack[-1][0] <= A[i]:
        stack.pop(-1)

    if len(stack) != 0:
        right[i] = stack[-1][1]

    stack.append((A[i], i))

answer = 0
for i in range(N):
    l = A[left[i]] if left[i] != -1 else 1e18
    r = A[right[i]] if right[i] != N else 1e18

    if l == 1e18 and r == 1e18:
        continue
    else:
        answer += min(l, r)

print(answer)