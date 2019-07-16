# 一つの種類は一つまでのナップサッック、重さ制限に加え個数制限がある
# メモ化再帰で解こうとしたが、TLE => 純粋なDPで試す => PyPyでMLE => ギリギリ通る

W = int(input()) 
N, K = map(int, input().split())

# v = []
# w = []
# for _ in range(N):
#     a, b = map(int, input().split())
#     w.append(a)
#     v.append(b)

# memo = [[[-1] * (K+1) for _ in range(W+1)] for _ in range(N+1)]

# i番目の品物から重さの総和がj以下で個数がk以下になるように選ぶ
# def rec(i, j, k):

#     if memo[i][j][k] >= 0:
#         return memo[i][j][k]

#     # 品物が残っていない or 個数制限に達する
#     if (i == N or k == K):
#         res = 0
#     # この品物は入らない
#     elif (j < w[i]):
#         res = rec(i + 1, j, k)
#     else:
#         # 入れる場合といれない場合を両方試す
#         res = max(rec(i + 1, j, k), rec(i + 1, j - w[i], k + 1) + v[i])
    
#     memo[i][j][k] = res
#     return res

# print(rec(0, W, 0))


# PyPyでMLEになるので、一番内側の要素数を最も大きいWとしている=> ほとんど影響ないがなぜかACした
# i個目まで見て、重さj以下で、選択個数kの場合の価値の最大値
dp = [[[0] * (W+1) for _ in range(K+1)] for _ in range(N+1)]

# dp[0][0][0] = 0 と考える

for i in range(1, N+1):
    w, v = map(int, input().split())
    for k in range(1, K+1):
        for j in range(1, W+1):
            # 重さが越えない場合
            if w <= j:
                # アイテムを選択した場合としていない場合で大きい方
                dp[i][k][j] = max(dp[i-1][k-1][j-w] + v, dp[i-1][k][j])
            else:
                dp[i][k][j] = dp[i-1][k][j]

print(dp[N][K][W])

