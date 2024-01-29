grapph = []

for i in range(19):
    grapph.append(list(map(int,input().split())))

def isOmok(i,j,graph):
    check = grapph[i][j]
    # 세로
    cnt = 0
    if i == 0 or graph[i-1][j] != check:
        for y in range(i,19):
            if graph[y][j] == check:
                cnt +=1

            else:
                if cnt ==5:
                    return (i,j)
                else:
                    break
        if cnt == 5:
            return (i, j)

    # 가로
    if j == 0 or graph[i][j-1] != check:
        cnt = 0
        for x in range(j,19):
            if graph[i][x] == check:
               cnt +=1
            else:
                if cnt == 5:
                    return(i,j)
                else:
                    break
        if cnt == 5:
            return (i, j)

    # 대각선 정방향
    if i == 0 or j == 0 or graph[i-1][j-1] != check:
        cnt = 0
        for k in range(0,19-max(i,j)):

            if graph[i+k][j+k] == check:
                cnt +=1
            else:
                if cnt ==5:
                    return (i,j)
                else:
                    break
        if cnt == 5:
            return (i, j)

    # 대각선 역방향
    if i == 18 or j == 0 or graph[i + 1][j -1] != check:
        cnt = 0
        for k in range(0,min(i,18-j+1)):
            if graph[i-k][j+k] == check:
                cnt +=1
            else:
                if cnt == 5:
                    return (i,j)
                else:
                    break
            if cnt == 5:
                return (i, j)

    return (-1,-1)

check = False
for i in range(19):
    for j in range(19):
        if grapph[i][j] != 0:
            temp = isOmok(i,j,grapph)
            if temp != (-1,-1):
                print(grapph[i][j])
                print(temp[0]+1,temp[1]+1)
                check = True
if check == False:
    print(0)

