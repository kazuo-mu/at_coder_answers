from queue import Queue

S = input()

ans = [0] * len(S)

R = Queue()
for i in range(len(S)):
    if S[i] == 'R':
        R.put(i)
    else:
        while not R.empty():
            r = R.get()
            l = i

            if abs(l - r) % 2 == 0:
                ans[i] += 1
            else:
                ans[i-1] += 1

L = Queue()
for i in range(len(S)-1, -1, -1):
    if S[i] == 'L':
        L.put(i)
    else:
        while not L.empty():
            l = L.get()
            r = i

            if abs(l - r) % 2 == 0:
                ans[i] += 1
            else:
                ans[i+1] += 1

print(' '.join(map(str, ans)))
