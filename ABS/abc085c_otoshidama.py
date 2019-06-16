N, Y = map(int, input().split())

answers = []

for i in range(0, N+1):
    for j in range(0, N+1-i):
        # print('{} {} {}'.format(i, j, k))
        # print(10000*i + 5000*j + 1000*k)
        if 10000*i + 5000*j + 1000*(N-i-j) == Y:
            answers.append('{} {} {}'.format(i, j, N-i-j))
                
if answers:
    print(answers[0])
else:
    print('-1 -1 -1')