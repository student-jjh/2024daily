N = int(input())
cnt = 0
answer = []
move = [(-1,0),(-1,-1),(-1,1)]
for_check = [[False for _ in range(N)] for _ in range(N)]


def check_Queen(i,j):
    for k in range(3):
        di = i + move[k][0]
        dj = j + move[k][1]
        while True:
            if di < 0 or di >=N or dj < 0 or dj >=N:
                break

            if for_check[di][dj] == True:
                return False

            di+= move[k][0]
            dj+= move[k][1]

    return True



def recur(si,num):
    global cnt

    if num == N:
        cnt +=1
        return

    for i in range(si,N):
        for j in range(0,N):
            if for_check[i][j] == False and check_Queen(i,j) == True:
                for_check[i][j] = True
                recur(i+1,num+1)
                for_check[i][j] = False
recur(0,0)

print(cnt)
