N, M = map(int, input().split())

e = []
for _ in range(M):
    e.append(tuple(map(int, input().split())))

e.sort(key=lambda x:x[1])


ans = 1
s, g = e[0]

for i in range(1, M):

    # 直近で最も小さい終点と、現在の始点を比較する
    if e[i][0] < g:
        continue
    else:
        g = e[i][1]
        ans += 1

print(ans)