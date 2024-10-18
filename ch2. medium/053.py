S = input()
mod = int(1e9 + 7)

answer = 0
power = 1
for i in range(len(S)):
    if S[i] == 'O':
        answer += power
        answer %= mod
    power *= 2
    power %= mod

print(answer)