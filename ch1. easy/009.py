import sys
input = sys.stdin.readline

N, M = map(int, input().split())
H = list(map(int, input().split()))

low = 0
high = max(H)

result = -1
while low <= high:
    mid = (low + high) // 2
    
    total = 0
    for h in H:
        if h > mid:
            total += h - mid
    
    if total < M:
        high = mid - 1
    else:
        result = mid
        low = mid + 1

print(result)