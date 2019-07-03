import copy

H = 10
W = 10
dxy_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]

org_field = []
field = []

# 全てを海と化す
def dfs(x, y):

    field[x][y] = 'x'
    
    for dxy in dxy_list:
        nx = x + dxy[0]
        ny = y + dxy[1]

        if 0 <= nx < H and 0 <= ny < W and field[nx][ny] == 'o':
            dfs(nx, ny)

    return

for _ in range(H):
    org_field.append(list(input()))


# 海に隣接する二つ以上の陸地がある際に、連結する陸全てを海と化す
# 全て海になれば成功
for x in range(H):
    for y in range(W):
        n_next = 0  # 隣接する陸の数

        for dxy in dxy_list:
            nx = x + dxy[0]
            ny = y + dxy[1]

            if 0 <= nx < H and 0 <= ny < W and org_field[nx][ny] == 'o':
                n_next += 1
            
        # 隣接する陸が2つ以上であれば全て海と化す
        field = copy.deepcopy(org_field)
        if n_next >= 2:
            dfs(x, y)

        success = True
        # フィールド全てが海になっていれば成功
        for i in range(H):
            for j in range(W):
                if field[i][j] == 'o':
                    success = False

        if success:
            print('YES')
            exit()

print('NO')

        
        