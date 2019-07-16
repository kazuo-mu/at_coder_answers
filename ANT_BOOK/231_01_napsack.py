# 一つの種類は一つまでのナップサック
# メモ化再帰で解く

N, W = map(int, input().split())

v = []
w = []
for _ in range(N):
    a, b = map(int, input().split())
    v.append(a)
    w.append(b)

memo = [[-1] * (W + 1) for _ in range(N+1)]

# i番目の品物から重さの総和がj以下となるように選ぶ
def rec(i, j):

    if memo[i][j] >= 0:
        return memo[i][j]

    # 品物が残っていない
    if (i == N):
        res = 0
    # この品物は入らない
    elif (j < w[i]):
        res = rec(i + 1, j)
    else:
        # 入れる場合といれない場合を両方試す
        res = max(rec(i + 1, j), rec(i + 1, j - w[i]) + v[i])
    
    memo[i][j] = res
    return res

print(rec(0, W))
