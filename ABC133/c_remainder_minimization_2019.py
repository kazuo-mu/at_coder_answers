# [i, j] の中に2019の倍数があれば、その倍数を選択すれば最小値を0

import math

L, R = map(int, input().split())
mod = 2019

# (A * B) % mod = (A % mod) * (B % mod) % mod
l = L % 2019
r = R % 2019

ans = None
# mod以上差があれば2019の倍数を含んでいる (ex. 2 & 2025)
if R - L >= mod:
    ans = 0
else:
    # mod以上差がなくても、あまりが0をまたぐ (ex. 2018 & 2025 => 2018 & 6) 場合
    if l > r:
        ans = 0
    else:
        _min = 2019 * 2019
        for i in range(l, r):
            for j in range(i+1, r+1):
                _min = min(_min, i*j%mod)
        ans = _min

print(ans)
