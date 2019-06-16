N = int(input())

schedule = [(0, 0, 0)]

canReach = True

for _ in range(N):
    t, x, y = map(int, input().split())
    schedule.append((t, x, y))

for i in range(N):
    _t = abs(schedule[i][0] - schedule[i+1][0])
    _x = abs(schedule[i][1] - schedule[i+1][1])
    _y = abs(schedule[i][2] - schedule[i+1][2])

    time = _t
    distance = _x + _y

    if time < distance:
        canReach = False
    # 時間に余裕がある場合でも、時間と距離の差分が偶数でなければ到達不可能
    else:
        if (time - distance) % 2 == 0:
            canReach = True
        else:
            canReach = False


if canReach:
    print('Yes')
else:
    print('No')
             
        
