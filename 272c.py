n = int(input())
a = list(map(int,input().split()))
dec_a = sorted(a, reverse=True)
ea = []
oa = []

for num in dec_a:
    if num%2 == 0:
        ea.append(num)
    else:
        oa.append(num)

if len(ea)<2 and len(oa)<2:
    print(-1)
elif len(ea)<2:
    print(oa[0]+oa[1])
elif len(oa)<2:
    print(ea[0]+ea[1])
else:
    if oa[0]+oa[1]<ea[0]+ea[1]:
        print(ea[0]+ea[1])
    else:
        print(oa[0]+oa[1])




    