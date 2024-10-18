N = int(input())
A = list(map(int, input().split()))

answer = 3

# shift 해서 정렬 시킬 수 있는지 확인
count = 0
for i in range(1, N):
    if A[i - 1] > A[i]:
        count += 1

if count <= 1 and A[0] > A[N - 1]:
    answer = 2

# 정렬 되어 있는지 확인
is_sorted = True
for i in range(1, N):
    if A[i - 1] > A[i]:
        is_sorted = False
        break

if is_sorted:
    answer = 1

print(answer)