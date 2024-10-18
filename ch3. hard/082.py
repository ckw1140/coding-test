A, B, C, D = input().split()

hands = ['R', 'S', 'P']

A = hands.index(A)
B = hands.index(B)
C = hands.index(C)
D = hands.index(D)

if A == B:
    if C == (A + 2) % 3 or D == (A + 2) % 3:
        print("TK")
    elif C == (A + 1) % 3 and D == (A + 1) % 3:
        print("MS")
    else:
        print("?")
elif C == D:
    if A == (C + 2) % 3 or B == (C + 2) % 3:
        print("MS")
    else:
        print("?")
else:
    print("?")