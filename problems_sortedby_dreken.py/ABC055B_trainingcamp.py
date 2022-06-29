n=int(input())
power=1
ans=0

for i in range(1,n+1):
    power*=i
    ans+=power%(10**9+7)

print(ans)