D, G = map(int, input().split())

N = []
C = []
for _ in range(D):
    n, c = map(int, input().split())
    N.append(n)
    C.append(c)

min_answered = 100**D + 5

# それぞれの配点の問題を完全に解くか、全く解かないかを決定する
for i in range(pow(2, D)):

    points = 0
    n_answered = 0
    rest_i = []  # 完全に解かない問題

    for j in range(D):
        # 2進数とした時、1であれば完全に解くとする
        if (i >> j) & 1:
            points += N[j] * (j+1) * 100 + C[j] # 問題数 x 配点 + ボーナス
            n_answered += N[j]

        # 全く解かない
        else:
            rest_i.append(j)

    # 全く解いていない配点の問題が残っている場合
    if rest_i:
        max_i = max(rest_i)  # 未完問題の最大添え字
        max_n = N[max_i]     # 未完最大配点問題の問題数
        max_p = 100 * (max_i + 1)  # 未完最大配点問題の点数

        # 目標に満たない場合、解いていない最大配点問題を中途半端に解く
        while points < G and max_n > 0:
            points += max_p
            n_answered += 1
            max_n -= 1

    # 目標を満たす場合のみ最小問題数を更新する
    if points >= G:
        min_answered = min(min_answered, n_answered)

print(min_answered)
N, M = map(int, input().split())

