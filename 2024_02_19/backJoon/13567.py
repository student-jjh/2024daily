M,n = map(int,input().split())
move = [(0,1),(1,0),(0,-1),(-1,0)]
order = []
for _ in range(n):
    order.append(list(map(str,input().split())))

i,j,status = 0,0,0
bk = False
for order,number in order:

    if order == "MOVE":
        di = i + move[status][0]*int(number)
        dj = j + move[status][1]*int(number)

        if di < 0 or di >= M or dj < 0 or dj >= M:
            print(-1)
            bk = True
            break
        i = di
        j = dj

    elif order == "TURN":
        if number == "0":

            status = (status + 1) % 4

        else :
             status -= 1
             if status <0:
                 status +=4


if bk == False:
    print(j,i)