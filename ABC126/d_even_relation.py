# 根をテキトーに選んで各頂点へのパスにおけるパリティを求める
# （なぜ根からで良いのかはパリティと木の性質によるもの）
# 答えはそのままパリティを出力する

from queue import Queue

# 隣接リスト、隣接コストを作る
n = int(input())

to = [[] for _ in range(n)]
cost = [[] for _ in range(n)]

for _ in range(n-1):
    u, v, w = map(int, input().split())

    # 各頂点の番号を添え字に合わせてデクリメントする
    # 答えに影響なし
    u-=1
    v-=1


    to[u].append(v)
    cost[u].append(w)

    to[v].append(u)
    cost[v].append(w)    


# 任意の点から初めてBFSで頂点をたどりながら、パリティを獲得していく
## BFS（queueに突っ込んでいって、なくなるまで頂点を辿っていく）

q = Queue()

ans = [-1] * n
q.put(0)

while not q.empty():
    u = q.get()
    
    for i in range(len(to[u])):
        v = to[u][i]
        w = cost[u][i]

        if (ans[v] != -1): continue

        ans[v] = (ans[u] + w) % 2
        q.put(v)
        

for a in ans:
    print(a)
        