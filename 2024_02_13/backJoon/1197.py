import heapq
V,E = map(int,input().split())
for_answer = set()
q = []
for _ in range(E):
    a,b,c = map(int,input().split())
    heapq.heappush(q,(c,a,b))
answer = 0
c,a,b = heapq.heappop(q)
for_answer.add(a)
for_answer.add(b)
answer += c
while len(for_answer) < V:
    c,a,b = heapq.heappop(q)
    print(c,a,b)

    if a not in for_answer or b not in for_answer:
        continue

    else:
        for_answer.add(a)
        for_answer.add(b)
        answer += c
print(for_answer)
print(answer)



