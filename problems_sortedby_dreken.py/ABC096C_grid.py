h,w=map(int,input().split())
grid_list=[]
flag=True
for i in range(h):
    grid_list.append(input())

for i in range(h):
    for ii in range(w):
        if grid_list[i][ii]=='#':
            if i==0:
                if ii==0:
                    if grid_list[i][ii:ii+2].count('#')<2 and grid_list[i+1][ii]!='#':
                        flag=False
                else:
                    if h==1:
                        if grid_list[i][ii-1:ii+2].count('#')<2:
                            flag=False
                    else:
                        if grid_list[i][ii-1:ii+2].count('#')<2 and grid_list[i+1][ii]!='#':
                            flag=False
            elif i==(h-1):
                if ii==0:
                    if grid_list[i][ii:ii+2].count('#')<2 and grid_list[i-1][ii]!='#':
                        flag=False
                else:
                    if grid_list[i][ii-1:ii+2].count('#')<2 and grid_list[i-1][ii]!='#':
                        flag=False
            else:
                if ii==0:
                    if grid_list[i][ii:ii+2].count('#')<2 and grid_list[i+1][ii]!='#' and grid_list[i-1][ii]!='#':
                        flag=False
                else:
                    if grid_list[i][ii-1:ii+2].count('#')<2 and grid_list[i+1][ii]!='#' and grid_list[i-1][ii]!='#':
                        flag=False

if flag:
    print('Yes')
else:
    print('No')