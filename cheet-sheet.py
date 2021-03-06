# 隣接リスト　作成
N, M = map(int, input().split())

to = []

for _ in range(N):
    a, b = map(int, input())
    to[a-1] = b-1
    to[b-1] = a-1


# Union-Find木, 結合＆判定リクエストを受ける
class UnionFind():

    def __init__(self, n):
        # 頂点の値が0から始まる前提なので注意
        self.par = [i for i in range(n)]

    def root(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return
        
        self.par[x] = y
        return
