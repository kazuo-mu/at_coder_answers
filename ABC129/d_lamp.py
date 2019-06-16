h, w = map(int, input().split())

s = []
for _ in range(h):
    s.append(list(input()))

cnt = [[0] * w for _ in range(h)]

for i in range(h):
    done = [0] * w
    for j in range(w):
        if s[i][j] == '#': continue
        if (done[j]): continue
    
        l = 0
        while j+l < w:
            if (s[i][j+l] == '#'): break
            l+=1

        for k in range(l):
            cnt[i][j+k] +=l
            done[j+k] = 1

for j in range(w):
    done = [0] * h
    for i in range(h):
        if s[i][j] == '#': continue
        if (done[i]): continue
    
        l = 0
        while i+l < h:
            if (s[i+l][j] == '#'): break
            l+=1

        for k in range(l):
            cnt[i+k][j] +=l
            done[i+k] = 1

_max = 0
for i in range(h):
    for j in range(w):
        _max =  max(cnt[i][j] - 1, _max)

print(_max)