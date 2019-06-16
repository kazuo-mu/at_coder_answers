h,w = map(int, input().split())

S = []

dxy_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for i in range(h):
    S.append(list(input()))


for i in range(h):
    for j in range(w):

        if (S[i][j] == '.'): continue
            
        has_sharp = False

        for dxy in dxy_list:
            ni = i + dxy[0]
            nj = j + dxy[1]

            if (ni < 0 or h <= ni): continue
            if (nj < 0 or w <= nj): continue

            if (S[ni][nj] == '#'):
                has_sharp = True
                break

        if (not has_sharp):
            print('No')
            exit()

print('Yes')
