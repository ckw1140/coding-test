N, L = map(int, input().split())

def is_good(number):
    while number > 0:
        if number % 10 == L:
            return False
        number //= 10
    return True

count = 1
number = 1 if L != 1 else 2
while count < N:
    number += 1

    if is_good(number):
        count += 1

print(number)