n = int(input())

a = list(map(int, input().split()))

# 負の数が偶数の時、全てのを非負に変換可能
# 奇数の時、一つを除いて非負に変換可能、絶対値が最小の値を選択する

cnt_minus = sum([1 if v < 0 else 0 for v in a])

list_abs = list(map(abs, a))
sum_abs = sum(list_abs)
min_abs = min(list_abs)

if cnt_minus % 2 == 0:
    ans = sum_abs
else:
    ans = sum_abs - 2*min_abs

print(ans)
    