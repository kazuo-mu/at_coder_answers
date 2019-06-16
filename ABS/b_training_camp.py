import math

n = int(input())

f = math.factorial(n)

print(f % (10**9 + 7))
