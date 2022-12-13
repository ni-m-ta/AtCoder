n,m = map(int,input().split())
roads = [[] for _ in range(n)]

for i in range(m):
    a,b = map(int,input().split())
    roads[a-1].append(b)
    roads[b-1].append(a)

for i in range(n):
    roads[i].sort()
    num = len(roads[i])
    print(num,end=' ')
    for j in range(num):
        if j == num-1:
            print(roads[i][j],end='')
        else:
            print(roads[i][j],end=' ')
    print()
