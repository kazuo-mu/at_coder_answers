N = int(input())
l = list(map(int, input().split()))

counter = 0

isAllEven = True

while True:
    for num in l:
        if (num % 2 != 0):
            isAllEven = False
    
    if (isAllEven == False): 
        break
    
    l = list(map(lambda n: n/2, l))
    counter+=1

print(counter)