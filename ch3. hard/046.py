import sys

input = sys.stdin.readline

T = int(input())
mod = (10 ** 9) + 7

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    B = [[]]
    for i in range(N):
        if A[i] == 0:
            B.append([])
        else:
            B[-1].append(A[i])

    
    answer_scale = 1
    answer_sign = -1
    for b in B:
        if len(b) == 0:
            continue

        scale = 0
        sign = 1
        for i in range(len(b)):
            if b[i] == -2 or b[i] == 2:
                scale += 1
            if b[i] == -2 or b[i] == -1:
                sign = -sign

            if sign == 1:
                if answer_sign == -1:
                    answer_sign = 1
                    answer_scale = scale
                else:
                    answer_scale = max(answer_scale, scale)
            elif answer_sign == -1:
                answer_scale = min(answer_scale, scale)

        scale = 0
        sign = 1
        for i in range(len(b) - 1, -1, -1):
            if b[i] == -2 or b[i] == 2:
                scale += 1
            if b[i] == -2 or b[i] == -1:
                sign = -sign

            if sign == 1:
                if answer_sign == -1:
                    answer_sign = 1
                    answer_scale = scale
                else:
                    answer_scale = max(answer_scale, scale)
            elif answer_sign == -1:
                answer_scale = min(answer_scale, scale)

    if answer_sign == 1:
        answer = 1
        for i in range(answer_scale):
            answer *= 2
            answer %= mod
        print(answer)
    else:
        if len(B) > 1:
            print(0)
        else:
            answer = 1
            for i in range(answer_scale):
                answer *= 2
                answer %= mod
            print(-answer)