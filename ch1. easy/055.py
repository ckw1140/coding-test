N = int(input())
S = input()

start = 0
end = 0
count = [0] * 26
num_types = 0

count[ord(S[0]) - ord('a')] = 1
num_types = 1

answer = 0
while start < len(S) and end < len(S):
    if num_types <= N:
        answer = max(answer, end - start + 1)
        end += 1
        if end < len(S):
            count[ord(S[end]) - ord('a')] += 1
            if count[ord(S[end]) - ord('a')] == 1:
                num_types += 1
    else:
        start += 1
        count[ord(S[start - 1]) - ord('a')] -= 1
        if count[ord(S[start - 1]) - ord('a')] == 0:
            num_types -= 1

print(answer)