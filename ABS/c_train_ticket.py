strs = list(input())

nums = list(map(int, strs))

op_patterns = []

ops = ['+', '-']

for op1 in ops:
    for op2 in ops:
        for op3 in ops:
            op_patterns.append((op1, op2, op3))


for pat in op_patterns:
    express = '{}{}{}{}{}{}{}'.format(nums[0], pat[0], nums[1], pat[1], nums[2], pat[2], nums[3])
    result = eval(express)

    if result == 7:
        print(express + '=7')
        exit()