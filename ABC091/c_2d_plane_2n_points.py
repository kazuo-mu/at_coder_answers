N = int(input())

reds = []
for _ in range(N):
    reds.append(tuple(map(int, input().split())))
    
blues = []
for _ in range(N):
    blues.append(tuple(map(int, input().split())))

reds.sort()
blues.sort()

ans = 0
for blue in blues:
    c, d = blue

    # 条件に当てはまる赤を抽出
    targets = [red for red in reds if red[0] < c and red[1] < d]
    targets.sort(key=lambda x:x[1])

    # 赤のうち一番y座標が大きいものを抽出
    if targets:
        target = targets.pop()
        reds.remove(target)
        ans += 1

print(ans)
