S = input()
T = input()

def find_basis(s):
    for i in range(1, len(s) + 1):
        if len(s) % i != 0:
            continue
        
        bad = False
        for j in range(i, len(s), i):
            if s[j:j + i] != s[:i]:
                bad = True
                break

        if not bad:
            return s[:i]

if find_basis(S) == find_basis(T):
    print(1)
else:
    print(0)