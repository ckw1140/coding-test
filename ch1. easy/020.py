N = int(input())
S = input()

T = ""
for i in range(N):
    if i == 0 or S[i] != S[i - 1]:
        T += S[i]

blue = 0
red = 0
for i in range(len(T)):
    if T[i] == 'B':
        blue += 1
    else:
        red += 1

if blue < red:
    print(1 + blue)
else:
    print(1 + red)