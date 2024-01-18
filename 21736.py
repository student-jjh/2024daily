N , M = map(int,input().split())
x,y = 0,0
answer = 0
mapOfUniv = []
move = [(1,0),(-1,0),(0,1),(0,-1)]

for i in range(N):
    temp_list = list(map(str,input().split("")))

    if "I" in temp_list :
        y = i
        x = temp_list.index("I")

    mapOfUniv.append(temp_list)

for i in range(4):
    dx,dy = x,y

    dx += move[i][0]
    dy += move[i][1]

    if dx > 0 and dy > 0 and dx < M and dy < N :
        pass
