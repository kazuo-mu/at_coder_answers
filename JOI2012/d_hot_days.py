D, N = map(int, input().split())
T = []
A = []
B = []
C = []

for _ in range(D):
    T.append(int(input()))

for _ in range(N):
    a, b, c = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)

# dp(i, j) : i日目にjの服を選んだ時の差の絶対値の合計
dp = [[-1] * N for _ in range(D)]

for i in range(N):
    if A[i] <= T[0] <= B[i]:
        dp[0][i] = 0

# 日ループ
for i in range(0, D-1):
    # 服ループ
    for j in range(0, N):
        # 気温的に選択可能であれば
        if A[j] <= T[i] <= B[j]:
            # 次の日の服ループ
            for k in range(0, N):
                if A[k] <= T[i+1] <= B[k]:
                    dp[i+1][k] = max(dp[i+1][k], dp[i][j] + abs(C[j] - C[k]))


print(max(dp[D-1]))
