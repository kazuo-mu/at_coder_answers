import queue

N, M = map(int, input().split())

S = []
for i in range(N):
    S.append(list(input()))

INF = 1000000000

SX = None
SY = None
GX = None
GY = None

for i in range(N):
    for j in range(M):
        if (S[i][j] == 'S'):
            SX = i
            SY = j
        
        if (S[i][j] == 'G'):
            GX = i
            GY = j

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs():

    d = [[INF] * M for _ in range(N)]

    que = queue.Queue()
    
    que.put((SX, SY))
    d[SX][SY] = 0
    
    while not que.empty():
        p = que.get()
        if (p[0] == GX and p[1] == GY): break
        
        for i in range(4):
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]


            if (0 <= nx and nx < N and 0 <= ny and ny < M and S[nx][ny] != '#'
                and d[nx][ny] == INF):
                que.put((nx, ny))
                d[nx][ny] = d[p[0]][p[1]] + 1
 
    return d[GX][GY]

print(bfs())
