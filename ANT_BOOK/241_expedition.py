import heapq

n, l, p = map(int, input().split())

A = []
for _ in range(n):
    A.append(int(input()))

B = []
for _ in range(n):
    B.append(int(input()))

# ゴールを追加
A.append(l)
B.append(0)
n += 1

que = []
ans = 0
pos = 0
tank = p

for i in range(n):
    d = A[i] - pos
    
    # ガソリンを補給
    while tank - d < 0:
        if not que:
            print(-1)
            exit()
        tank += -heapq.heappop(que)
        ans+=1
    
    tank -= d
    pos = A[i]
    heapq.heappush(que, -B[i])

print(ans)