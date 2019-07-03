# 隣接リスト　作成
N, M = map(int, input().split())

to = []

for _ in range(N):
    a, b = map(int, input())
    to[a-1] = b-1
    to[b-1] = a-1

