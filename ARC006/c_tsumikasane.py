N = int(input())
W = []

for _ in range(N):
    W.append(int(input()))

W.reverse()
tops = []  # ダンボール山の頂上だけ管理

while W:
    w = W.pop()

    if tops:
        diffs = [top - w for top in tops]
        
        idx = None
        min_diff = 100005
        
        # ダンボールに載せれて、最もダンボールの頂上との差分が小さい山を探す
        for i in range(len(diffs)):
            if diffs[i] >= 0 and diffs[i] < min_diff:
                min_diff = diffs[i]
                idx = i

        # 山が見つかれば頂上を更新する
        if idx != None:
            tops[idx] = w
        # なければ、新しく山を作る
        else:
            tops.append(w)

    else:
        tops.append(w)

print(len(tops))

