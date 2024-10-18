N = int(input())
A = list(map(int, input().split()))

psum0 = [0] * N
psum1 = [0] * N

psum0[0] = A[0]
psum1[0] = 0
for i in range(1, N):
    psum0[i] = psum0[i - 1]
    psum1[i] = psum1[i - 1]
    if i % 2 == 0:
        psum0[i] += A[i]
    else:
        psum1[i] += A[i]

answer = psum0[N - 1]

for i in range(N):
    sum = 0
    if i > 0:
        sum += psum0[i - 1]
    sum += psum1[N - 2]
    if i > 0:
        sum -= psum1[i - 1]
    if i % 2 == 0:
        sum += A[N - 1]

    answer = max(answer, sum)
        
print(answer)