x,a,b=map(int,input().split())
all_sum=0

for i in range(1,x+1):
    each_sum=0
    i=str(i)
    for ii in range(len(i)):
        each_sum+=int(i[ii])
    if each_sum>=a and each_sum<=b:
        all_sum+=int(i)

print(all_sum)