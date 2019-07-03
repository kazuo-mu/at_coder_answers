S = input()
n = len(S)

is_hard = False

for i in range(1, n):
    if S[i-1] == S[i]:
        is_hard = True
    
if is_hard:
    print('Bad')
else:
    print('Good')