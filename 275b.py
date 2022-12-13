nums = list(map(int,input().split()))
fr = 1
lt = 1

for i in range(6):
    if i < 3:
        fr *= nums[i]%998244353
    else:
        lt *= nums[i]%998244353

print((fr-lt)%998244353)