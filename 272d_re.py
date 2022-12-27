n,m = map(int,input().split())
board = [[0]*n]

for i in range(1,n+1):
    a = 1
    b = 1
    count = 0
    for j in range(1,n+1):
        while a > 0 and a <= n and b > 0 and b <= 0
            if a = i and b = j:
                board[i-1][j-1] = count
                continue
            else:
                (i-a)**2 + (j-b)**2 == m
                a=i
                b=j
                count += 1
print(board)
'''
for i in range(n):
    for j in range(n):
        if j == n-1:
            print(board[i][j])
        else:
            print(board[i][j],end=' ')
'''