N, P, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if P == Q:
    possible = True
    for i in range(N):
        if A[i] != B[i]:
            possible = False
            break
    if possible:
        print("YES")
        for i in range(N):
            print(0, end=" ")
    else:
        print("NO")
else:
    if P > Q:
        P, Q = Q, P
        for i in range(N):
            A[i], B[i] = B[i], A[i]

    answer = []
    possible = True
    for i in range(N):
        if A[i] == B[i]:
            answer.append(0)
        elif A[i] > B[i]:
            if (A[i] - B[i]) % (Q - P) == 0:
                answer.append((A[i] - B[i]) // (Q - P))
            else:
                possible = False
                break
        else:
            possible = False
            break

    if possible:
        print("YES")
        for i in range(N):
            print(answer[i], end=" ")
    else:
        print("NO")