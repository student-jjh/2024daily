N,S = map(int,input().split())



temp = list(map(int,input().split()))
temp.append(0)

start = end = 0
sm = temp[start]
for_answer = 100001
while end != N:
    if sm >= S:
        for_answer = min(end - start+1, for_answer)

        sm -= temp[start]
        start +=1

    else:
        end +=1
        sm += temp[end]
if for_answer == 100001:
    for_answer = 0
print(for_answer)