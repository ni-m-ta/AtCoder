h,w=map(int,input().split())
str_list=[]
mine_list=[]

for i in range(h):
    str_list.append(input())

for i in range(h):
    for ii in range(w):
        count=0
        if str_list[i][ii]=='.':
            if ii==0:
                if i!=0:
                    count+=str_list[i-1][ii:ii+2].count('#')
                count+=str_list[i][ii:ii+2].count('#')
                if i!=(h-1):
                    count+=str_list[i+1][ii:ii+2].count('#')
                mine_list.append(count)
            else:
                if i!=0:
                    count+=str_list[i-1][ii-1:ii+2].count('#')
                count+=str_list[i][ii-1:ii+2].count('#')
                if i!=(h-1):
                    count+=str_list[i+1][ii-1:ii+2].count('#')
                mine_list.append(count)
        else:
            mine_list.append(str_list[i][ii])

for i in range(1,h*w+1):
    print(mine_list[i-1],end='')
    if i%w==0:
        print('')