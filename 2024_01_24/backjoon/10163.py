N = int(input())


mi = 0
mj = 0
for_anwer = [0 for _ in range(N+1)]
temp = []
for K in range(1,N+1):
    _i,_j,w,h = map(int,input().split())
    mi = max(mi,_i+h)
    mj = max(mj,_j+w)
    temp.append((_i,_j,w,h))


graph = [[0 for _ in range(mj+1)] for _ in range(mi+1)]

for K in range(1,len(temp)+1):
    _i, _j, w, h = temp[K-1]
    for i in range(_i,_i +h):
        for j in range(_j,_j + w):
            graph[i][j] = K

for i in range(1,N+1):
    for line in graph:
        for_anwer[i] += line.count(i)

for item in for_anwer[1:]:
    print(item)




