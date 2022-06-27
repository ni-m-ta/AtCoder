n=int(input())
nums_board=list(map(int,input().split()))
count=-1

flag=True
while flag:
    for i in range(n):
        if nums_board[i]%2!=0:
            flag=False
        else:
            nums_board[i]/=2 
    count+=1

print(count)