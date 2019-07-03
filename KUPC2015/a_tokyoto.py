N = int(input())

ans = []

for _ in range(N):
    word = list(input())
    n = len(word)
    cnt = 0

    i = 0
    while i < n:
        if word[i] in ('t', 'k'):
            if ''.join(word[i:i+5]) in ('tokyo', 'kyoto'):
                i += 4
                cnt += 1
        
        i +=1
    
    ans.append(cnt)

for a in ans:
    print(a)
            