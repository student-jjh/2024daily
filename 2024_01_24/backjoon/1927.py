import heapq
import sys
input =sys.stdin.readline

N = int(input().strip())

q = []

for i in range(N):
    n = int(input().strip())

    if n == 0 :
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q,n)
