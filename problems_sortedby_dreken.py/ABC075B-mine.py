h,w=map(int,input().split())
str_list=[]
mine_list=[]

for i in range(h):
    str_list.append(input())

for i in range(h):
    for ii in range(w):
        count=0
        if str_list[i][ii]=='.':
            count+=str_list[i][ii-1:ii+2].count('#')
            mine_list.append(count)
        else:
            mine_list.append(str_list[i][ii])

print(mine_list)