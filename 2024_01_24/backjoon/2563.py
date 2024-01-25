N = int(input())

main_lst = [[0 for i in range(100)] for j in range(100) ]

for _ in range(N):
    x,y = map(int,input().split())

    for w in range(x,x+10):
        for e in range(y,y+10):
            main_lst[w][e] = 1

answer = 0

for temp in main_lst:
    answer += temp.count(1)

print(answer)