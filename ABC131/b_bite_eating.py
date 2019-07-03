N, L = map(int, input().split())

pie = 0
min_abs = 10000
min_abs_apple = None
for i in range(N):
    if min_abs > abs(i + L):
        min_abs = abs(i + L)
        min_abs_apple = i + L
    pie += i + L

print(pie - min_abs_apple)