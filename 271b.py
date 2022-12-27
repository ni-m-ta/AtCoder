n,q = map(int,input().split())
ls = [list(map(int,input().split())) for _ in range(n)]
qs = [list(map(int,input().split())) for _ in range(q)]

for i in range(q):
    print(ls[qs[i][0]-1][qs[i][1]])