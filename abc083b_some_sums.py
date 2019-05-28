N, A, B = map(int, input().split())

targets = []

for i in range(N):
    s = str(i+1)
    digits = list(map(int, s))
    sum_digits = sum(digits)
    
    if (sum_digits >= A and sum_digits <= B):
        targets.append(i+1)
        
print(sum(targets))
