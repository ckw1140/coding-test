N, A, B = map(int, input().split())

players = list(range(1, N + 1))

round = 1
found = False
while True:
    winners = []
    for i in range(0, len(players) - 1, 2):
        # i, i + 1
        if players[i] in [A, B] and players[i + 1] in [A, B]:
            found = True
            break
        if players[i] in [A, B]:
            winners.append(players[i])
        else:
            winners.append(players[i + 1])
    
    if len(players) % 2 == 1:
        winners.append(players[-1])

    if found:
        break

    players = winners
    round += 1

print(round)