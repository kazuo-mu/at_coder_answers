N, Q = map(int, input().split())

RW = []
for i in range(N):
    RW.append(list(map(int, input().split())))

D = []
for i in range(Q):
    D.append(int(input()))

RW.sort(key=lambda x:x[2])  # 工事中の座業でソート

for i in range(Q):  # Q人
    stop = False
    for j in range(N):  # N工事数
        s, t, x = RW[j]
        if (s <= x + D[i]) and (x + D[i] < t):
            print(RW[j][2])
            stop = True
            break
    
    if not stop:
        print(-1)