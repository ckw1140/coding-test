import sys
input = sys.stdin.readline

N = int(input())
A = [int(input()) for _ in range(N)]

def max_sum(a):
    left = [-1] * N
    right = [N] * N

    stack = []
    for i in range(N):
        while len(stack) > 0 and a[stack[-1]] <= a[i]:
            stack.pop(-1)
        
        if len(stack) > 0:
            left[i] = stack[-1]

        stack.append(i)

    stack = []
    for i in range(N - 1, -1, -1):
        while len(stack) > 0 and a[stack[-1]] < a[i]:
            stack.pop(-1)

        if len(stack) > 0:
            right[i] = stack[-1]

        stack.append(i)

    answer = 0
    for i in range(N):
        answer += (i - left[i]) * (right[i] - i) * a[i]

    return answer

print(max_sum(A) + max_sum([-A[i] for i in range(N)]))