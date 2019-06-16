s = list(input())

N = 15
n = len(s)
rest_n = N - n

win_n = sum([1 if s[i] == 'o' else 0 for i in range(len(s))])

remaining_win_n = 8 - win_n

if rest_n >= remaining_win_n:
    print('YES')
else:
    print('NO')
