# 1) K回優先度付きキューにPush(log_N) : K * logN
# 2) ヒープソート(N*log_N) = ルートをN回削除（log_N）
# 1) + 2) = (K + N) * log_N

import queue

q = queue.PriorityQueue()
N, K = map(int, input().split())
A = []
B = []

for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

# 機械の(初期値, 番号)をPush
for i in range(N):
    q.put((A[i], i))
     
ans = 0
for i in range(K):
    p, j = q.get()
    ans += p
    q.put((p + B[j], j))

print(ans)
