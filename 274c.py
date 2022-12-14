n = int(input())
amebas = list(map(int,input().split()))

ans = [0]*(2*n+1)

for i,a in enumerate(amebas):
    ans[2*i+1]=ans[a-1]+1
    ans[2*i+2]=ans[a-1]+1

for i in range(2*n+1):
    print(ans[i])

# 二本木の考え方
