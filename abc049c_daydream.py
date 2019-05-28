S = input()

words = ['dream', 'dreamer', 'erase', 'eraser']

canTryNext = True

while canTryNext:
    canTryNext = False
    for word in words:
        if S.endswith(word):
            canTryNext = True
            len_word = len(word)
            S = S[:len(S)-len_word]
    
if not S:
    print('YES')
else:
    print('NO')