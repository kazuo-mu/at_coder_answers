from queue import Queue

H, W = map(int, input().split())
N = H * W
field = []

dxy_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]

INF = 10000
cost = [[INF] * W for _ in range(H)]

for _ in range(H):
    field.append(list(input()))

n_black = 0
for r in field:
    for c in r:
        if c == '#':
            n_black += 1

que = Queue()
que.put((0,0))
cost[0][0] = 1

while not que.empty():
    x, y = que.get()

    if x == H-1 and y == W-1:
        break

    for dxy in dxy_list:
        nx = x + dxy[0]
        ny = y + dxy[1]

        if 0 <= nx < H and 0 <= ny < W and field[nx][ny] != '#' and cost[nx][ny] == INF:
            que.put((nx, ny))
            cost[nx][ny] = cost[x][y] + 1    

if cost[H-1][W-1] == INF:
    print(-1)
    exit()

print(N - n_black - cost[H-1][W-1])