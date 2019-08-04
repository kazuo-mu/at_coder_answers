from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

dic = defaultdict(int)


# 3の倍数個
if N % 3 == 0:
    
    for a in A:
        dic[a] += 1

    n_kind = len(dic.keys())
    values = list(dic.keys())
    cnts = list(dic.values())
        
    # 整数の種類数で分岐
    if n_kind == 3:
        is_xor = False    
        # 3つの整数で xorの関係を作れるか判定
        for i in range(n_kind-2):
            for j in range(i+1, n_kind-1):
                for k in range(j+1, n_kind):
                    if values[i] ^ values[j] ^ values[k] == 0:
                        is_xor = True

        
        # 3つの整数がそれぞれ N/3個であるか判定
        is_n_valid = True
        for cnt in cnts:
            if cnt != N/3:
                is_n_valid = False

            
        if is_xor and is_n_valid:
            print('Yes')
        else:
            print('No')
    
    elif n_kind == 2:
        
        # 2つの整数がそれぞれ 2N/3個であり、0がN/3子であるか判定
        is_n_valid = True
        if 0 in values:
            for k, v in dic.items():
                if k == 0:
                    if v != N/3:
                        is_n_valid = False
                else:
                    if v != N * (2/3):
                        is_n_valid = False
        else:
            is_n_valid = False

        if is_n_valid:
            print('Yes')
        else:
            print('No')


    elif n_kind == 1:
        all_zero = True
        for a in A:
            if a != 0:
                all_zero = False

        if all_zero:
            print('Yes')
        else:
            print('No')        

    else:
        print('No')

# 3の倍数個以外の場合は、全て0である必要がある
else:
    all_zero = True
    for a in A:
        if a != 0:
            all_zero = False

    if all_zero:
        print('Yes')
    else:
        print('No')
           