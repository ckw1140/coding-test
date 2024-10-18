N, M = map(int, input().split())
MAX_VAL = 1000000001

stuff = {}
for _ in range(N):
    name, cost = input().split()
    cost = int(cost)
    stuff[name] = cost

formulas = [input() for _ in range(M)]

for i in range(M):
    result, formula = formulas[i].split('=')

    if result not in stuff:
        stuff[result] = -1

    elements = formula.split('+')
    for e in elements:
        k = int(e[0])
        name = e[1:]

        if name not in stuff:
            stuff[name] = -1

while True:
    update = False
    for i in range(M):
        result, formula = formulas[i].split('=')

        computable = True
        value = 0
        elements = formula.split('+')
        for e in elements:
            k = int(e[0])
            name = e[1:]

            if stuff[name] == -1:
                computable = False
                break
            else:
                value += k * stuff[name]
                value = min(value, MAX_VAL)
        
        if computable:
            if stuff[result] == -1 or stuff[result] > value:
                stuff[result] = value
                update = True

    if not update:
        break

if "LOVE" in stuff and stuff["LOVE"] != -1:
    print(stuff["LOVE"])
else:
    print(-1)