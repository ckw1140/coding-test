X, Y = map(int, input().split())

days = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
yoil = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

m = 1
d = 1
id = 0

while m != X or d != Y:
    d += 1
    id = (id + 1) % 7

    if d == days[m] + 1:
        m += 1
        d = 1

print(yoil[id])