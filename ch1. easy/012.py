import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

mistake = [1 if A[i] > A[i + 1] else 0 for i in range(N - 1)]
psum = [0] * (N - 1)
for i in range(N - 1):
    if i == 0:
        psum[i] = mistake[i]
    else:
        psum[i] = psum[i - 1] + mistake[i]

Q = int(input())
for _ in range(Q):
    x, y = map(int, input().split())
    x -= 1
    y -= 1

    if x == y:
        print(0)
        continue
    
    # x ~ y-1
    answer = psum[y - 1]
    if x > 0:
        answer -= psum[x - 1]
    
    print(answer)