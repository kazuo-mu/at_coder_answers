N = int(input())
L = list(map(int, input().split()))

ans = 0

# 板が最後の一つになるまで
while N > 1:

    # 一番短い板mii1, 次に短い板mii2を求める
    mii1 = 0; mii2 = 1
    
    # 戦略
    # 初期値はテキトーに左端の二つとする
    # ソートせず、リスト全体を見てテキトーに決めた最小の板より小さいものがあれば取り替える

    if L[mii1] > L[mii2]: mii1, mii2 = mii2, mii1

    for i in range(2, N, 1):
        if L[i] < L[mii1]:
            mii2 = mii1
            mii1 = i
        elif L[i] < L[mii2]:
            mii2 = i

    t = L[mii1] + L[mii2]
    ans += t

    # mii1が右端ならば、mii2を右端とする
    if mii1 == N - 1:
        mii1, mii2 = mii2, mii1
    # mii1の値をtotal値で上書きする（mii1の値はもう必要ない）
    L[mii1] = t
    # mii2の値を右端の値で上書きする（mii2の値はもう必要ないし、右端を削りたいので）
    N -= 1

print(ans)

