from collections import deque

X = int(input())
S = input()
S = list(S)

count = {'M': 0, 'W': 0}
answer = len(S)
while len(S) > 0:
    if len(S) >= 2 and count[S[0]] > count[S[1]]:
        count[S.pop(1)] += 1
    else:
        count[S.pop(0)] += 1

    if abs(count['M'] - count['W']) > X:
        answer = count['M'] + count['W'] - 1
        break

print(answer)