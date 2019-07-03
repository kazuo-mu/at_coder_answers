# 再帰の回数のせいでREになる

H, W = map(int, input().split())
city = []

for _ in range(H):
    city.append(list(input()))

dxy_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
can_reach = False

def dfs(x, y):
    
    city[x][y] = '#'
    
    for dxy in dxy_list:
        nx = x + dxy[0]
        ny = y + dxy[1]

        if 0 <= nx and nx < H and 0 <= ny and ny < W:
            if city[nx][ny] == '.':
                dfs(nx, ny)

            elif city[nx][ny] == 'g':
                global can_reach
                can_reach = True
                return

    return


for i in range(H):
    for j in range(W):
        if city[i][j] == 's':
            dfs(i, j)
            

if can_reach:
    print('Yes')
else:
    print('No')