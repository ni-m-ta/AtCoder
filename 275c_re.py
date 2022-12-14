board = [input() for _ range(9)]
porns = []
for i in range(9):
    for j in range(9):
        if board[i][j] == '#':
            porns.append([i,j])

n = len(porns)
for i in range(n):
    for j in range(n):
        for k in range(n):
            for l in range(n):
                if porns[i][0]<=porns[j][0] and porns[i][1]<porns[j][1]:
                    if porns[k][0]<=porns[l][0] and porns[k][1]<porns[l][1] and porns[i][0]<porns[k][0]:
                        if porns[i][0]-porns[j][0] == porns[k][0]-porns[0] 

