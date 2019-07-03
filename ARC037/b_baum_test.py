# TODO: 「頂点数 -1 = エッジ数 であれば、木」を試すがWA
# 「訪問済みに訪問しようとすれば、閉路あり」も試したがWA

N, M = map(int, input().split())
 
to = [[] for _ in range(N)]
visited = [False for _ in range(N)]
n_tree = 0
cnt_v = 0   # 連結部分の頂点数
cnt_e = 0   # 連結部分のエッジ数
last_v = None
 
def dfs(u):
    global cnt_v, cnt_e, last_v
    cnt_v += 1  # 訪問した頂点を数える
    visited[u] = True
    
    for v in to[u]:
        if v == last_v:
            continue

        cnt_e += 1  # 訪れたかどうかを問わずエッジを数える
        if not visited[v]:
            last_v = u
            dfs(v)
    return
 
 
# 隣接リスト
for _ in range(M):
    u, v = map(int, input().split())
    to[u-1].append(v-1)
    to[v-1].append(u-1)
 
 
# 全ての未訪問の頂点に対して
for i in range(N):
    if not visited[i]:
        cnt_v = 0
        cnt_e = 0
        dfs(i)
 
        if cnt_e == cnt_v - 1:
            n_tree += 1
 
print(n_tree)