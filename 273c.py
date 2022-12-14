n = int(input())
a = list(map(int,input().split()))
a.sort()
a_set = set(a)

ans = [0]*n
for i in range(n):
    if a[i] in a_set:
        a_set.remove(a[i])
    ans[len(a_set)] += 1

for i in range(n):
    print(ans[i])
    

