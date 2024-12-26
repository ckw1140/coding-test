N = int(input())

longgest = []
for i in range(1, N + 1):
    numbers = [N, i]
    while numbers[-1] >= 0:
        numbers.append(numbers[-2] - numbers[-1])
    numbers.pop(-1)

    if len(longgest) < len(numbers):
        longgest = numbers[:]

print(len(longgest))
print(*longgest)
