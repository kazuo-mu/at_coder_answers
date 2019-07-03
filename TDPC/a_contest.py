# メモ化再帰

N = int(input())
P = list(map(int, input().split()))

memo = []

# num番目(Pの(num-1)番目)でvalを作れるか
def can_make(num, val):

    # メモ化されていればメモ値を返す
    if (memo[num][val] != -1):
        return memo[num][val] == 1

    # 0番目で作れるのは0だけ
    if (num == 0): return val == 0
    
    # val-P[num-1]が負になる場合は, valのみチェック
    if (val - P[num-1]) < 0:
        if can_make(num-1, val):
            memo[num][val] = 1
            return True
        else:
            memo[num][val] = 0
            return False
    else:
        if can_make(num-1, val - P[num-1]) or can_make(num-1, val):
            memo[num][val] = 1
            return True
        else:
            memo[num][val] = 0
            return False


def main():
    _sum = sum(P)

    global memo
    memo = [[-1] * (_sum+1) for _ in range(N+1)]

    ans = 0
    for i in range(_sum+1):
        if can_make(N, i):
            ans += 1
    
    print(ans)


if __name__ == '__main__':
    main()