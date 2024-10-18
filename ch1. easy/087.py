S = input()
T = input()

stack = []
for i in range(len(S)):
    stack.append(S[i])

    if len(stack) >= len(T):
        same = True
        for j in range(len(T)):
            if stack[-len(T) + j] != T[j]:
                same = False
                break
        if same:
            for _ in range(len(T)):
                stack.pop(-1)

if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))