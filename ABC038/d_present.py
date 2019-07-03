# TODO: 部分点のみAC

N = int(input())

wh = []
for _ in range(N):
    wh.append(tuple(map(int, input().split())))

wh.sort()

INF = N + 5
dp = [INF] * N
dp[0] = 1

ans = 1

for i in range(N):
    dp[i] = 1
    for j in range(i):
        if wh[j][0] < wh[i][0] and wh[j][1] < wh[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

    ans = max(ans, dp[i])

print(ans)