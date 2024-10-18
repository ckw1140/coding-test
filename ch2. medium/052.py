l = int(input())
r = int(input())
k = int(input())

# 1 ~ r -> 나타낼 수 있는 수들
# 1 ~ l-1 -> 나타낼 수 있는 수들
# 위 - 아래 l~r -> ...

if k == 2:
    upper = max(0, r - 2)
    lower = max(0, l - 3)
    print(upper - lower)
elif k == 3:
    upper = max(0, r // 3 - 1)
    lower = max(0, (l - 1) // 3 - 1)
    print(upper - lower)
elif k == 4:
    # 2의 배수, 10 이상, 12는 표현 못함
    upper = max(0, r // 2 - 4)
    lower = max(0, (l - 1) // 2 - 4)

    if r >= 12:
        upper -= 1
    if l - 1 >= 12:
        lower -= 1

    print(upper - lower)    
else:
    upper = max(0, r // 5 - 2)
    lower = max(0, (l - 1) // 5 - 2)
    print(upper - lower)