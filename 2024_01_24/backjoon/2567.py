paper = [[0 for _ in range(101)] for _ in range(101)]
move = [(1,0),(0,1),(-1,0),(0,-1)]
N = int(input())

for i in range(N):
    a,b = map(int,input().split())

    for j in range(a,a+10):
        for k in range(b,b+10):
            paper[j][k] = 1

ans = 0
for i in range(101):
    for j in range(101):
        cnt = 0
        if paper[i][j] == 1:
            for k in range(4):
                di = i + move[k][0]
                dj = j + move[k][1]

                if 0<=di<101 and 0<=dj<101:
                    if paper[di][dj] == 1 :
                        cnt +=1

        if cnt ==2:
            ans += 2
        if cnt ==3:
            ans +=1
print(ans)
