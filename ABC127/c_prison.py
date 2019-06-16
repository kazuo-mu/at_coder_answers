N, M = map(int, input().split())

L = []
R = []
for i in range(M):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

l_max = max(L)
r_min = min(R)

if l_max <= r_min:
    print(r_min - l_max + 1)
else:
    print(0)
