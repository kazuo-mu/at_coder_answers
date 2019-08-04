import math

n, d = map(int, input().split())

width = 2 * d + 1

print(math.ceil(n / width))