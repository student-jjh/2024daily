bingo = []

def is_bingo(graph):
    cnt = 0
    for i in graph:
        if i == [0,0,0,0,0]:
            cnt +=1

    temp = list(zip(*graph))

    for i in temp:
        if i == (0,0,0,0,0):
            cnt +=1
    for_c = 0
    for_cc = 0
    for i in range(5):
        if graph[i][i] == 0:
            for_c +=1
        if graph[i][4-i] == 0:
            for_cc +=1
    if for_c == 5:
        cnt +=1
    if for_cc == 5:
        cnt +=1

    if cnt >=3:
        return True
    else:
        return False

for _ in range(5):
    bingo.append(list(map(int,input().split())))

call = []

for _ in range(5):
    call.append(list(map(int,input().split())))

cnt = 0
stop = False
for i in range(5):
    for j in range(5):
        cnt +=1
        word = call[i][j]
        for k in range(5):
            if word in bingo[k]:
               bingo[k][bingo[k].index(word)] = 0

        if is_bingo(bingo) == True:
            print(cnt)
            stop = True
            break
    if stop:
        break
