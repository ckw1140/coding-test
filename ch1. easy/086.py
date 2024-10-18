S = input()

count = [0] * 26
for i in range(len(S)):
    if ord('a') <= ord(S[i]) and ord(S[i]) <= ord('z'):
        count[ord(S[i]) - ord('a')] += 1
    else:
        count[ord(S[i]) - ord('A')] += 1

max_count = 0
who = -1
for i in range(26):
    if max_count < count[i]:
        max_count = count[i]
        who = i
    elif max_count == count[i]:
        who = -1

if who == -1:
    print("?")
else:
    print(chr(who + ord('A')))