import heapq

x, y, z, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

e = []

# AxB を取得
for va in a:
    for vb in b:
        heapq.heappush(e, -(va+vb))

# AxB は 大きい方から最大k個のみ使う
d = []
ite = min(k, len(e))

# AxB[k個] x C を取得
for i in range(ite):
    ve = -heapq.heappop(e)
    for vc in c:
        heapq.heappush(d, -(ve+vc))

for i in range(k):
    print(-heapq.heappop(d))
