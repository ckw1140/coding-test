N = int(input())
A = list(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))

def solve(A, B):
    I = list(set(A) & set(B))

    if len(I) == 0:
        return []
    else:
        max_val = max(I)

        A_prime = A[A.index(max_val) + 1:]
        B_prime = B[B.index(max_val) + 1:]

        return [max_val] + solve(A_prime, B_prime)

answer = solve(A, B)
print(len(answer))
print(*answer)