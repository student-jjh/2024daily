N = int(input())


answer = 0

for i in range(N+1):
    for j in range(60):
        for k in range(60):
            check = str(i) + str(j) + str(k)

            if '3' in check:
                answer +=1

print(answer)

