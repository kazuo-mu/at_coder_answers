import bisect
from collections import deque

N = int(input())

tops = deque()

for i in range(N):
    a = int(input())
    p = bisect.bisect_left(tops, a)
    
    if p == 0:
        # bisect.insort_left(tops, a)
        # Atcoder上だとエラーになる？？
        
        # appendleftしてもソート順は崩れないので、こっちの方が良い
        tops.appendleft(a)
    else:    
        tops[p-1] = a
        
print(len(tops))
