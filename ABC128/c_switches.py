N, M = map(int, input().split())

n_switches = []
switches = []
for i in range(M):
    ipt = list(map(int, input().split()))
    n_switches.append(int(ipt[0]))
    switches.append(ipt[1:])


p = list(map(int, input().split()))

ans = 0

# print(n_switches)
# print(switches)
# print(p)

# ランプの光り方のパターンだけ
for i in range(2 ** N):
    ptn = bin(i)[2:].rjust(N, '0')

    allLight = True  # 全ての電球が光っているかどうか（一つでも光っていなければそのパターンは無効）

    # 電球の数だけ
    for j in range(M):

        n_light = 0
        # 電球に対するスウィッチの数だけ
        for k in range(n_switches[j]):
            # スウィッチが光っていれば
            if ptn[switches[j][k] - 1] == '1':
                n_light += 1

        if n_light % 2 != p[j]:
            allLight = False
            break

    if allLight:
        ans += 1

print(ans)

    