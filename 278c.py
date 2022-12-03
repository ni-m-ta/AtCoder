import sys
imput = sys.stdin.readline
n,q = map(int,input().split())
twidai = set()
for i in range(q):
    t,a,b = map(int,input().split())
    if t == 1:
        twidai.add((a,b))
    elif t == 2:
        twidai.discard((a,b))
    else: # t == 3
        if {(a,b), (b,a)} <= twidai:
            print('Yes')
        else:
            print('No')
