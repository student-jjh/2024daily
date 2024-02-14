N = int(input())
visited = [False for _ in range(N+1)]
mp,mf,ms,mv = map(int,input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int,input().split())))
# 조건 충족 했는지 구해주는 함수 따로 빼기
def good_health(lst):
    _p,_f,_s,_v = 0,0,0,0
    for i in lst:
        _p += graph[i][0]
        _f += graph[i][1]
        _s += graph[i][2]
        _v += graph[i][3]

    if _p < mp or _f < mf or _s < ms or _v < mv:
        return False
    return True

answer = 100000000
answer_lst = []
lst = []

def recur(si,num):
    global answer
    global answer_lst
    # 멈추는 조건? + 계산까지
    if good_health(lst) == True:
        temp = 0
        for i in lst:
            temp += graph[i][4]
        if temp < answer:
            answer = temp
            answer_lst = lst[:]
        return

    for j in range(si,N):
        if visited[j] == False:
            visited[j] = True
            lst.append(j)
            recur(j+1,num+1)
            lst.pop()
            visited[j] = False
recur(0,0)
if answer == 100000000:
    print(-1)
else:
    print(answer)
    answer_lst = [i+1 for i in answer_lst]
    print(*answer_lst)