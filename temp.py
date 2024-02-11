N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))
cnt1 = 0
cnt2 = 0
temp1 = []
temp2 = []
start = 0
for i in range(N):
    start = start^1 
    for j in range(start,N,2):
        if graph[i][j] == 1:
            temp1.append((i,j))
            cnt1 +=1
start = 1
for i in range(N):
    start = start^1 
    for j in range(start,N,2):
        if graph[i][j] == 1:
            temp2.append((i,j))
            cnt2 +=1
          

num = 0

v1 = [False for _ in range(N*2)]
v2 = [False for _ in range(N*2)]




check = []
for_check = set()
answer = 0
real_answer = 0
def recur(si,num,temp,cnt):
    global answer

    if num > answer:
        answer = num
    if answer == min(N*2 - 2,cnt):
        return
    for i in range(si,cnt):
        if v1[temp[i][0] + temp[i][1]] == False and v2[temp[i][0] - temp[i][1]] == False:
            v1[temp[i][0] + temp[i][1]] = True
            v2[temp[i][0] - temp[i][1]] = True
            recur(i+1,num +1,temp,cnt)
            v1[temp[i][0] + temp[i][1]] = False
            v2[temp[i][0] - temp[i][1]] = False
recur(0,num,temp1,cnt1)
real_answer += answer
answer = 0
recur(0,num,temp2,cnt2)
real_answer += answer
print(real_answer)