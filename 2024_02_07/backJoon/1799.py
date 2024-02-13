N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))
cnt = 0
temp = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            temp.append((i,j))
            cnt +=1
num = 0
visited = [False for _ in range(cnt)]
v1 = [False for _ in range(N*2)]
v2 = [False for _ in range(N*2)]
if (0,0) in temp or (N-1,N-1) in temp:
    try:
        temp.remove((0,0))
        cnt -= 1
    except:
        pass
    try:
        temp.remove((N - 1, N - 1))
        cnt -= 1
    except:
        pass
    v2[0] = True
    num +=1

if (0,N-1) in temp or (N-1,0) in temp:
    try:
        temp.remove((0,N-1))
        cnt -= 1
    except:
        pass
    try:
        temp.remove((0, N - 1))
        cnt -= 1
    except:
        pass
    v1[N-1] = True
    num +=1

check = []
for_check = set()
answer = 0
def recur(si,num):
    global answer

    if num > answer:
        answer = num
    if answer == min(N*2 - 2,cnt):
        return
    for i in range(si,cnt):
        if v1[temp[i][0] + temp[i][1]] == False and v2[temp[i][0] - temp[i][1]] == False:
            v1[temp[i][0] + temp[i][1]] = True
            v2[temp[i][0] - temp[i][1]] = True
            recur(i+1,num +1)
            v1[temp[i][0] + temp[i][1]] = False
            v2[temp[i][0] - temp[i][1]] = False
recur(0,num)
print(answer)
