a,b,c,d=map(int,input().split())

if a<=c:
    if b<=d:
        holding_time=b-c
    else:
        holding_time=d-c
else:
    if b<=d:
        holding_time=b-a
    else:
        holding_time=d-a

if holding_time<0:
    holding_time=0

print(holding_time)