for _ in range(3):
    S = input()

    count = 1
    max_count = 1
    for i in range(1, len(S)):
        if S[i] == S[i - 1]:
            count += 1
        else:
            count = 1
        max_count = max(max_count, count)

    print(max_count)