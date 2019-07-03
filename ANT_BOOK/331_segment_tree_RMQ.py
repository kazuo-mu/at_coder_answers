MAX_N = 1 << 17

# セグメント木を持つグローバル配列
dat = [0 for _ in range(2 * MAX_N -1)]

# 初期化
def init(int n_):

    # 簡単のため、要素数を２のべき乗に
    n = 1
    while (n < n_): n *= 2

    INF = 1000000000
    for i in range(2 * n -1): dat[i] = INF
    

# k番目の値(0-indexed)をaに変更
def update(k, a):

     # 葉の節点
     k += n - 1
     dat[k] = a
     # 登りながら更新
     while (k > 0):
        k = (k - 1) // 2
        dat[k] = min(dat[k * 2 + 1], dat[k * 2 + 2])
    

# [a, b)の最小値を求める
# 後ろの方の引数は、計算の簡単のため
# kは節点の番号, l, rはその節点が[l, r)に対応づいていることを示す
# したがって、外からはquery(a, b, 0, 0, n)として呼ぶ
def query(a, b, k, l, r):
    # [a, b)と[l, r)が交差しなければ、INT_MAX
    if (r <= a || b <= 1):  return INT_MAX
    
    # [a, b)が[l, r)を完全に含んでいれば、この節点の値
    if (a <= l && r <= b): return dat[k]
    else:
        # そうでなければ、二つの子の最小値
        vl = query(a, b, k * 2 + 1, l, (l + r) / 2)
        vr = query(a, b, k * 2 + 2, (l + r) / 2, r)
        return min(vl, vr)
