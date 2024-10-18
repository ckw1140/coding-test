S = input()


robot = -1
goal = -1
order = []
for i in range(len(S)):
    if S[i] in ['@', '#', '!']:
        order.append(S[i])
    if S[i] == '@':
        robot = i
    if S[i] == '!':
        goal = i

if order[1] == '#':
    print(abs(robot - goal) - 1)
else:
    print(-1)