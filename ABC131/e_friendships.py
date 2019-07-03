N, K = map(int, input().split())

lower = 0
upper = (N-1) * (N-2) / 2

ans = []

if lower <= K  and K <= upper:

    for i in range(1, N):
        for j in range(i+1, N+1):
            ans.append((i, j))

    k = 0
    while k < K:
        del ans[-1]
        k += 1

    print(len(ans))

    for ptn in ans:
        print('{} {}'.format(ptn[0], ptn[1]))


    # 距離が２の点の組を表示する
    # res = []
    # n = len(ans)

    # for i in range(n):
    #     for j in range(i+1, n):
    #         if ans[i][1] == ans[j][0]:
    #             res.append((ans[i][0], ans[j][1]))        

    # for r in res:
    #     print('{} {}'.format(r[0], r[1]))

else:
    print('-1')