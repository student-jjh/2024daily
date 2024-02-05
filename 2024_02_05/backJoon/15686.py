def chicken_lenght(house,left):
    global answer
    ans = 0
    for home in house:
        temp = 10000000
        for chick in left:
            check =  abs(home[0] - chick[0]) + abs(home[1] - chick[1])
            if temp > check:
                temp = check
        ans += temp
        if ans > answer:
            break

    return ans



def broke_chicken(si,num):
    global answer
    if num == M :
        answer= min(answer,chicken_lenght(house,left))
        return

    for i in range(si,len(chicken_house)):
        if vt[i] == False:
            left.append(chicken_house[i])
            vt[i] = True
            broke_chicken(i+1,num+1)
            vt[i] = False
            left.pop()


N,M = map(int,input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

house = []
chicken_house = []


for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            house.append((i,j))
        elif graph[i][j] == 2:
            chicken_house.append((i,j))

vt = [False for _ in range(len(chicken_house))]
left = []
answer = 10000000

broke_chicken(0,0)
print(answer)