# Stack バージョン　通った

H, W = map(int, input().split())
city = []

for _ in range(H):
    city.append(list(input()))

dxy_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]        
can_reach = False

stack = []

for i in range(H):
    for j in range(W):
        if city[i][j] == 's':
            stack.append((i, j))
            break

    if stack:
        break

while stack:
    x, y = stack.pop()

    city[x][y] = '#'
    
    for dxy in dxy_list:
        nx = x + dxy[0]
        ny = y + dxy[1]

        if 0 <= nx and nx < H and 0 <= ny and ny < W:
            if city[nx][ny] == '.':
                stack.append((nx, ny))

            elif city[nx][ny] == 'g':
                can_reach = True
                break

    if can_reach:
        break

if can_reach:
    print('Yes')
else:
    print('No')