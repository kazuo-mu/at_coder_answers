N = int(input())

AB = []

for _ in range(N):
    AB.append(tuple(map(int, input().split())))



AB.sort(key=lambda x:x[1])

on_time = True

time = 0
for ab in AB:
    a = ab[0]
    b = ab[1]

    time += a

    if time > b:
        on_time = False

if on_time:
    print('Yes')
else:
    print('No')