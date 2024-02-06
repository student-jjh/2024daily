N = int(input())

temp = list(map(int,input().split()))

dic = {}

for item in temp:
    dic[item] = 1

M = int(input())

temp2 = list(map(int,input().split()))
answer = [0 for _ in range(M)]

for i in range(M):
    if temp2[i] in dic:
        answer[i] =1

print(*answer)
