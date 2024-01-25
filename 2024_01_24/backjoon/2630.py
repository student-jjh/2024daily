from collections import deque

# a = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
#
#
# print([b[2:4] for b in a[2:4]] )
grade = [0,0]
def check_all(graph):
    for_check = graph[0][0]
    for line in graph:
        for item in line:
            if item != for_check:
                return False
    return True


N = int(input())
graph = []

for i in range(N):
    graph.append(list(map(int,input().split())))

queue  = deque()
queue.append(graph)
while queue:
    temp = queue.popleft()

    if check_all(temp):
        grade[temp[0][0]] +=1
    else:
        N = len(temp) //2
        queue.append(list(k[0:N] for k in temp[0:N]))
        queue.append(list(k[N:N+N] for k in temp[N:N+N]))
        queue.append(list(k[0:N] for k in temp[N:N+N]))
        queue.append(list(k[N:N+N] for k in temp[0:N]))

for item in grade:
    print(item)