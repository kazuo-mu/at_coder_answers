from collections import defaultdict

S = input()

kind = defaultdict(int)

for s in S:
    kind[s] += 1

if len(kind) == 2:
    f = True
    for k in kind.values():
        if k != 2:
            f = False
    
    if f:
        print('Yes')
    else:
        print('No')
else:
    print('No')
