a, b, c, d = map(int, input().split())

lower = max(a,c)
upper = min(b,d)

print(max(upper-lower, 0))
