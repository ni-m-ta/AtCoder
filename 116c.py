n = int(input())
hs = list(map(int,input().split()))
count = 0
flag = True
beg = 0
while flag:
    for i in range(beg,n):
        if hs[i] == 0:
            beg == i+1
            break
        else:
            hs[i] -= 1
    count += 1
    print(hs)
    if sum(hs) == 0:
        flag = False
print(count)