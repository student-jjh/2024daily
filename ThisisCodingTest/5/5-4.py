T = int(input())

for _ in range(T):
    N ,M = map(int,input().split())

    temp = list(map(int,input().split()))

    graph = []

    for i in range(0,N*M,M):
        graph.append(temp[i:i+M])
    
    graph = list(zip(*graph))

    A, B, C = graph[0]

    for line in graph[1:]:
        a,b,c = line

        a= a + max(A,B)
        b = b + max(A,B,C)
        c = c + max(B,C)

        A,B,C = a,b,c
    
    print(max(A,B,C))