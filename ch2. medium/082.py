S = input()

stack = []
for i in range(len(S)):
    stack.append(S[i])

    while len(stack) >= 4 and "".join(stack[-4:]) == "PPAP":
        for _ in range(3):
            stack.pop(-1)

if len(stack) == 1 and stack[0] == 'P':
    print("PPAP")
else:
    print("NP")