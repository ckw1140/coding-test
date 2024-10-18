N = int(input())


low = 0
high = 2**32

while low <= high:
    mid = (low + high) // 2

    if mid**2 < N:
        low = mid + 1
    else:
        ans = mid
        high = mid - 1

print(ans)