T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()

    def sol():
        count = 0
        for a in range(N - 2):
            c = a + 2
            for b in range(a + 1, N):
                while c < N and A[c] - A[b] < A[b] - A[a]:
                    c += 1
                
                if c < N and A[c] - A[b] == A[b] - A[a]:
                    count += 1
        return count

    print(sol())