N = 5
graph = []
move = [(1,0),(-1,0),(0,1),(0,-1)]
check = 0
for _ in range(N):
    temp = list(input())
    check += temp.count("Y")
    graph.append(temp)

if check >= 22 :
    print(0)

elif check <=3:
    print(3546)

else:
    def check_in(i,j,lst):
        temp = set(lst)
        for k in range(4):
            di = i + move[k][0]
            dj = j + move[k][1]

            if di < 0 or di >=N or dj < 0 or dj >=N:
                continue

            if (di,dj) in temp :
                return True
        return False

    def recur(num,lst,y_count):
        if y_count >3:
            return
        if num == 7:
            temp = lst[:]
            temp.sort()
            temp = tuple(temp)
            if temp not in answers:
                answers.add(temp)
            return

        for k in range(0,25):
            i = k //5
            j = k % 5
            if visited[i][j] == False and (check_in(i,j,lst) or lst ==[]):
                visited[i][j] = True
                lst.append((i,j))
                if graph[i][j] == "Y":
                    recur(num+1,lst,y_count+1)
                else:
                    recur(num + 1, lst, y_count)
                visited[i][j] = False
                lst.pop()

    lst = []
    answers = set()
    visited = [[False for _ in range(N)] for _ in range(N)]
    recur(0,lst,0)
    print(len(answers))

