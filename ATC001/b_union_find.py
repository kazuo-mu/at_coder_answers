N, Q = map(int, input().split())

par = [i for i in range(100000)]


def root(x):
    if par[x] == x:
        return x
    else:
        par[x] = root(par[x])
        return par[x]

def same(x, y):
    return root(x) == root(y)

def unite(x, y):
    x = root(x)
    y = root(y)

    if x == y:
        return
    
    par[x] = y
    return

def main():
    reqs = []
    for _ in range(Q):
        req = tuple(map(int, input().split()))
        reqs.append(req)

    for req in reqs:
        p, a, b = req

        # p=0: 結合リクエスト
        if p == 0:
            unite(a, b)
        # p=1: 判定リクエスト
        elif p == 1:
            if same(a, b):
                print('Yes')
            else:
                print('No')


if __name__ == '__main__':
    main()
