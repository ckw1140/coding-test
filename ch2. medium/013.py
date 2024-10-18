N = int(input())

count = 0
for _ in range(N):
    S = input()

    stack = []
    for s in S:
        if len(stack) == 0 or stack[-1] != s:
            stack.append(s)
        else:
            stack.pop(-1)

    if len(stack) == 0:
        count += 1

print(count)