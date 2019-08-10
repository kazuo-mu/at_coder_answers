import heapq

N = int(input())

q = []

for _ in range(N):
    s = input()
    ss = sorted(s)
    heapq.heappush(q, ss)



n = 1
last = ''
ans = 0

while q:
    v = heapq.heappop(q)
    if v == last:
        n += 1
    else:
       ans += n*(n-1) // 2
       n =1

    last = v

if n != 0:
    ans += n*(n-1) // 2
    

print(ans)