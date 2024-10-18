N = int(input())

count = {}
for _ in range(N):
    title = input()

    if title not in count:
        count[title] = 0
    count[title] += 1

max_value = 0
max_title = ""
for key, value in count.items():
    if max_value < value:
        max_value = value
        max_title = key
    elif max_value == value and max_title > key:
        max_title = key

print(max_title)