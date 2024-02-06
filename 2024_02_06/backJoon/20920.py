N,M = map(int,input().split())

dict ={}

for _ in range(N):
    temp = input()
    if len (temp) <M:continue
    if temp in dict:
        dict[temp] +=1

    else:
        dict[temp] = 1

for_answer = list(dict.items())
for_answer.sort()
for_answer.sort(reverse = True,key = lambda x : len(x[0]))
for_answer.sort( reverse=True, key = lambda x : x[1])

for item in for_answer:
    print(item[0])