R,C = map(int,input().split())

graph = []

for i in range(R):
    temp = list(input())
    if "S" in temp:
        start = (i,temp.index("S"))
    graph.append(temp)
