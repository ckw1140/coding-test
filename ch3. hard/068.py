N, M = map(int, input().split())
trie = [[-1] * 26]
num_nodes = 1

for _ in range(N):
    S = input()

    u = 0
    for s in S:
        if trie[u][ord(s) - ord('a')] == -1:
            trie[u][ord(s) - ord('a')] = num_nodes
            trie.append([-1] * 26)
            num_nodes += 1
        u = trie[u][ord(s) - ord('a')]

answer = 0
for _ in range(M):
    S = input()

    found = True
    u = 0
    for s in S:
        if trie[u][ord(s) - ord('a')] == -1:
            found = False
            break
        u = trie[u][ord(s) - ord('a')]

    if found:
        answer += 1

print(answer)