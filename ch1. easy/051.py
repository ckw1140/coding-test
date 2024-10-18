N = int(input())

min_name = "ZZZ"
for _ in range(N):
    name = input()

    if len(name) == 3:
        min_name = min(min_name, name)

print(min_name)