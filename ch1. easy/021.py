T = int(input())

for _ in range(T):
    S = input()

    if len(S) < 3:
        print("Good")
        continue

    if S[0] != 'A':
        if S[0] not in {'A', 'B', 'C', 'D', 'E', 'F'}:
            print("Good")
            continue
        S = S[1:]
    if S[-1] != 'C':
        if S[-1] not in {'A', 'B', 'C', 'D', 'E', 'F'}:
            print("Good")
            continue
        S = S[:-1]

    T = ""
    for i in range(len(S)):
        if i == 0 or S[i] != S[i - 1]:
            T += S[i]

    if T == "AFC":
        print("Infected!")
    else:
        print("Good")