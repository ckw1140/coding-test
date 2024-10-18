N = int(input())
U = input()


def solve(a, b):
    lcp = len(a)
    for i in range(len(a)):
        if a[i] != b[i]:
            lcp = i
            break
    
    lcs = len(a)
    for i in range(len(a)):
        if a[-i - 1] != b[-i - 1]:
            lcs = i
            break

    return lcp + lcs >= len(a)


if len(U) % 2 == 0:
    print("NOT POSSIBLE")
else:
    half = len(U) // 2

    answer = []
    if solve(U[:half], U[half:]):
        answer.append(U[:half])
    if solve(U[half + 1:], U[:half + 1]):
        answer.append(U[half + 1:])

    answer = list(set(answer))

    if len(answer) == 0:
        print("NOT POSSIBLE")
    elif len(answer) != 1:
        print("NOT UNIQUE")
    else:
        print(answer[0])