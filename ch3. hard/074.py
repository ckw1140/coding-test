T = int(input())

def evaluate(s):
    s = s.replace(' ', '')
    return eval(s)

for _ in range(T):
    N = int(input())

    answer = []
    for mask in range(3 ** (N - 1)):
        S = ""
        tmp = mask
        for i in range(N - 1):
            S += str(i + 1)
            if tmp % 3 == 0:
                S += "+"
            elif tmp % 3 == 1:
                S += "-"
            else:
                S += " "
            tmp //= 3
        S += str(N)

        if evaluate(S) == 0:
            answer.append(S)

    answer.sort()
    for s in answer:
        print(s)
    print()
        