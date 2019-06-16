N = int(input())
M = int(input())
S = list(input())
T = list(input())

dp = [[0] * (M+1) for _ in range(N+1)]

for i in range(N):
    for j in range(M):
        if (S[i] == T[j]):
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

print(dp[N][M])