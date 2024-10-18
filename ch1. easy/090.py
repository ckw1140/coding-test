N = int(input())
A = list(map(int, input().split()))

stack = []
answer = [-1] * N
for i in range(N - 1, -1, -1):
    while len(stack) > 0 and stack[-1] <= A[i]:
        stack.pop(-1)

    if len(stack) > 0:
        answer[i] = stack[-1]

    stack.append(A[i])

print(*answer)