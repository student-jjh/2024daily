N = int(input())

for_check = [ x**2 for x in range(1,27)]
print(for_check)
for_answer = []
i=j=sm = 0
sm= for_check[0]
while j < 25 :
    if sm == N :
        for_answer.append(j-i+1)

    if sm < N:
        j +=1
        sm += for_check[j]

    else:
        sm -= for_check[i]
        i +=1

print(for_answer)
