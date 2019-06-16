n = int(input())

up = list(map(int, input().split()))
down = list(map(int, input().split()))

points = []

for i in range(n):
    point = sum(up[:i+1]) + sum(down[i:])
    points.append(point)

print(max(points))