s = input()
n = len(s)

# パターン数
for i in range(2**(n-1)):
    
    exp = s[0]

    # 右シフトする
    for j in range(1, n):
        if (i >> j-1) & 1:
            exp += '+'
        else:
            exp += '-'
        
        exp += s[j]

    if eval(exp) == 7:
        print('{}=7'.format(exp))
        exit()