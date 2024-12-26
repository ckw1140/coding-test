A, B, C, D = map(int, input().split())

diff = 1e9
diff = min(diff, abs(A + B - C - D))
diff = min(diff, abs(A + C - B - D))
diff = min(diff, abs(A + D - B - C))
print(diff)
