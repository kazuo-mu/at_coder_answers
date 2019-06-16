N = int(input())
S = []

for i in range(N):
    city, point = input().split()
    point = int(point)
    s = (city, point, i+1)
    S.append(s)

S.sort(key=lambda x: x[1], reverse=True)

S.sort(key=lambda x: x[0])

for s in S:
    print(s[2])