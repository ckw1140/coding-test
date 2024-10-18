A, B, C, M = map(int, input().split())

piro = 0
work = 0
for _ in range(24):
    if piro + A > M:
        piro -= C
        piro = max(0, piro)
    else:
        piro += A
        work += B

print(work)