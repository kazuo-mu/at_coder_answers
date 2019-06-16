import math

n = int(input())

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

bn = min(a, b, c, d, e)

print(4 + math.ceil(n / bn))
