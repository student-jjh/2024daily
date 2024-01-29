N = int(input())

temp = []
for i in range(N):
    temp.append(int(input()))


cnt =1
mx =temp.pop()


while temp:
    item = temp.pop()
    if item > mx:
        mx = item
        cnt +=1

print(cnt)
