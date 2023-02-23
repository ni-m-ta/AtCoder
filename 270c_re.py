n,x,y = map(int,input().split())
vs = [[] for _ in range(n+1)]

for _ in range(n-1):
    u,v = map(int,input().split())
    vs[u].append(v)
    vs[v].append(u)

for i in range(n-1):
    vs[i].sort()

seen = [False for _ in range(n+1)]
ans = []
def dfs(graph, v, goal):
    seen[v] = True
    if v == goal:
        ans.append(v)
        for i in range(len(ans)):
            if i == len(ans)-1:
                print(ans[i])
            else:
                print(ans[i],end=' ')
        exit()
    for i in range(0,len(graph[v])):
        if seen[graph[v][i]]:
            continue
        ans.append(v)
        dfs(graph, graph[v][i], goal)
        ans.pop()

# 探索し尽くしてかつゴールに行かないときに初めてpopにたどり着いて誤った道を消す、そして一つ前に戻る

dfs(vs, x, y)

