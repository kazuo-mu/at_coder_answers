import queue

H, W = map(int, input().split())
F = []
for _ in range(H):
    F.append(list(input()))

dxy_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
q = queue.Queue()
INF = 1000000
cost = [[INF] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if F[i][j] == '#':
            q.put((i, j))
            cost[i][j] = 0

while not q.empty():
    
    x, y = q.get()
    for dxy in dxy_list:
        nx = x + dxy[0]
        ny = y + dxy[1]

        if 0 <= nx < H and 0 <= ny < W and F[nx][ny] == '.':
            F[nx][ny] = '#'
            cost[nx][ny] = cost[x][y] + 1
            q.put((nx, ny))


max_c = 0
for i in range(H):
    for j in range(W):
        max_c = max(max_c, cost[i][j])
    
print(max_c)
        
            
        