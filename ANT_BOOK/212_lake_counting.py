N, M = map(int, input().split())

field = []

for i in range(N):
    s = list(input())
    field.append(s)    

def dfs(x, y):
    field[x][y] = '.'
    
    # 8方向を探索
    for dx in range(-1, 2, 1):
        for dy in range(-1, 2, 1):
            nx = x + dx
            ny = y + dy

            if (0 <= nx and nx < N and 0 <= ny and ny < M and field[nx][ny] == 'W'):
                dfs(nx, ny)
    
    return

res = 0

for i in range(N):
    for j in range(M):
        if field[i][j] == 'W':
            dfs(i, j)
            res += 1

print(res)