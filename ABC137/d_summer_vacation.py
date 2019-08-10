import heapq
from collections import defaultdict

N, M = map(int, input().split())

jobs = []
cnts = defaultdict(int)
rets = []


# 全ての仕事をヒープへ挿入
for i in range(N):
    a, b = map(int, input().split())

    heapq.heappush(jobs, (a, -b))
    cnts[a] += 1


ans = 0

# M日後のi日前において、選択可能な仕事の報酬を候補としてヒープへ登録する
# 各日付において候補の中からどれでも一つ選択可能な状態
for i in range(1, M+1):

    cnt = cnts.get(i)

    if cnt:
        while cnt > 0:
            a, b = heapq.heappop(jobs)
            heapq.heappush(rets, b)
            cnt -= 1

    if rets:
        b = heapq.heappop(rets)
        ans -= b

print(ans)