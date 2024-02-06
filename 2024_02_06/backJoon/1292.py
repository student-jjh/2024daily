A,B = map(int,input().split())

temp = [0]

for i in range(1,50):
    for j in range(i):
        temp.append(i)

print(sum(temp[:B+1])-sum(temp[:A]))
