n =  int(input())
x_list = []

def ToBi(x):
    bi = 0
    pos = 1
    while x >= 1:
        a = x%2
        bi += a*pos
        pos *= 10
        x //= 2
    return bi

def IntToStr(x):
    return str(x)

def Check(x, n):
    flag = True
    for i in range(len(x)):
        if n[len(n)-i-1] == '0':
            if x[len(x)-i-1] == '1':
                flag = False
                break
    return flag




bi_n_str = str(ToBi(n))

for x in range(n+1):
    x_str = IntToStr(ToBi(x))
    if Check(x_str, bi_n_str):
        print(x)




    
