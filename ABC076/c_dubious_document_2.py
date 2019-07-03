S = input()
T = input()


def match(k):
    s = S[k:k+len(T)]
    
    for j in range(len(s)):
        if s[j] not in (T[j], '?'):
            return False

    return True

def construct(k):
    ans = list(S)

    for i in range(len(T)):
        ans[k+i] = T[i]
    
    for i in range(len(S)):
        if (ans[i] == '?'):
            ans[i] = 'a'

    return ''.join(ans)

res = []
for i in range(len(S) - len(T) + 1):
    if match(i):
        s = construct(i)
        res.append(s)

if res:
    print(min(res))
else:
    print('UNRESTORABLE')
