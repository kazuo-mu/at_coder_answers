n, k = map(int, input().split())
s = list(map(int, input()))

now = 1
cnt = 0
nums = []

for i in range(n):
    if s[i] == now: cnt+=1
    else:
        nums.append(cnt)
        now = 1 - now  # 0, 1の切り替え
        cnt = 1  # カウントを始める

if cnt != 0: nums.append(cnt)

# 計算しやすさのため、1の個数-0の個数...1の個数という配列が欲しい
if (len(nums) % 2 == 0): nums.append(0)

add = 2 * k + 1
tmp_sum = 0

left = 0
right = 0

ans = 0

for i in range(0, len(nums), 2):

    next_left = i
    next_right = min(i + add, len(nums))

    while left < next_left:
        tmp_sum -= nums[left]
        left+=1

    while right < next_right:
        tmp_sum += nums[right]
        right+=1

    ans = max(tmp_sum, ans)

print(ans)


