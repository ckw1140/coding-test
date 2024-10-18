from itertools import permutations

N = int(input())

qna = []
for i in range(N):
    qna.append(input().split())


count = 0
for permutation in permutations(range(1, 10), 3):
    good = True
    for i in range(N):
        strike = 0
        ball = 0
        # 스트라이크 세기
        for j in range(3):
            if int(qna[i][0][j]) == permutation[j]:
                strike += 1
                continue
            if int(qna[i][0][j]) in permutation:
                ball += 1
        
        if strike != int(qna[i][1]):
            good = False
            break
        if ball != int(qna[i][2]):
            good = False
            break
    if good:
        count += 1

print(count)