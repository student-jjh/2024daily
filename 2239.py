# 스도쿠.. 메직 스타 문제와 비슷하게 접근하면 되나?
# 리스트를 총 27개를 활용해서 체크 수행?
# 하나의 좌표에 총 3개 리스트를 확인해야 함
# 백트레킹을 27개..?
# 0,1,2 는 3으로 나누면 몫이 0 3,4,5는 3으로 나누면 몫이 1이걸 이용해서 어떤 리스트 확인해야 하는지 확인

# 세로로 1~9 확인용
N_lst = [[False for _ in range(10)]for _ in range(9)]
# 가로로 1~9 확인용
M_lst = [[False for _ in range(10)]for _ in range(9)]

# 가로세로 3X3으로 1~9 확인용
NM_lst = [[[False for _ in range(10)] for _ in range(3)]for _ in range(3)]

graph = []
for _ in range(9):
    graph.append(list(map(int,list(input()))))

need_to_fill = []

for i in range(9):
    for j in range(9):
        if graph[i][j] != 0:
            N_lst[i][graph[i][j]] = True
            M_lst[j][graph[i][j]] = True
            NM_lst[i//3][j//3][graph[i][j]] = True

        else:
            need_to_fill.append([i,j])

stop = len(need_to_fill)
stop_sign = False
def recur(num):
    global stop_sign
    if stop_sign == True:
        return
    if num == stop:
        for line in graph:
            temp = list(map(str,line))
            print("".join(temp))
        stop_sign = True
        return
    
    for i in range(1,10):
        ci,cj = need_to_fill[num]
        if N_lst[ci][i] == False and M_lst[cj][i] == False and NM_lst[ci//3][cj//3][i] == False:
            N_lst[ci][i] = True
            M_lst[cj][j] = True
            NM_lst[ci//3][cj//3][i] = True
            graph[ci][cj] = i
            recur(num+1)
            graph[ci][cj] = 0
            N_lst[ci][i] = False
            M_lst[cj][j] = False
            NM_lst[ci//3][cj//3][i] = False

recur(0)