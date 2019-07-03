## ACしない、4つRE

N = int(input())
V = 100005

to = [[] for _ in range(V*2)]
visited = [False] * (V*2)
cnt = [0, 0]

# 連結している二部グラフ(X, Y)の頂点数を数える
def dfs(v):
    if visited[v]: return
    visited[v] = True
    cnt[v//V] += 1
    for u in to[v]: dfs(u)


ans = 0

# 二部グラフの作成
for i in range(N):
    x, y = map(int, input().split())
    y += V
    to[x].append(y)
    to[y].append(x)


for i in range(V*2):
    if (visited[i]): continue
    cnt = [0, 0]
    dfs(i)
    ans += cnt[0] * cnt[1]

ans -= N
print(ans)
    