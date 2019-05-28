H, W = map(int, input().split())

S = []

dxy_list = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

for _ in range(H):
    S.append(list(input()))

for i in range(H):
    for j in range(W):
        if(S[i][j] == '#'): continue
        
        num = 0
        for dxy in dxy_list:
            ni = i + dxy[0]
            nj = j + dxy[1]

            if (ni < 0 or H <= ni): continue
            if (nj < 0 or W <= nj): continue
            
            if(S[ni][nj] == '#'): num += 1

        S[i][j] = str(num)

for row in S:
    print(''.join(row))
