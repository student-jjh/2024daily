N, M = map(int,input().split())

temp = set()
temp2 = set()

for i in range(N):
    temp.add(input())
for j in range(M):
    temp2.add(input())

temp3 = temp.intersection(temp2)
temp3 = list(temp3)
temp3.sort()
print(len(temp3))
for name in temp3:
    print(name)