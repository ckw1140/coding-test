S = input()

num_k = 0
num_r = 0
for i in range(len(S)):
    if S[i] == 'K':
        num_k += 1
    if S[i] == 'R':
        num_r += 1


start = -1
end = len(S)

max_length = 0
for i in range(num_k // 2 + 1):
    if num_r == 0:
        break
    # k가 i개 있을 때,
    max_length = max(max_length, 2 * i + num_r)

    start += 1
    end -= 1
    while start < end and S[start] == 'R':
        start += 1
        num_r -= 1
    while start < end and S[end] == 'R':
        end -= 1
        num_r -= 1

print(max_length)