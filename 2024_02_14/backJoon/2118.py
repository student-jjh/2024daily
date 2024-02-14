# 아이디어는, 처음에는 모두 시계 방향으로 설정하고, 입력 은 sys로 받아야 할듯?
import sys

input = sys.stdin.readline

N = int(input())

lst = []
sm = 0
for _ in range(N):
    temp = int(input())
    lst.append(temp)
    sm += temp
lst.append(0)

start,end = 0,0
ssmm = lst[0]
answer = 0
while end != N:
    temp_answer = min(ssmm,sm - ssmm)
    if temp_answer > answer:
        answer = temp_answer
    if ssmm == sm - ssmm:
        answer = ssmm
        break

    if ssmm < sm - ssmm:
        end +=1
        ssmm += lst[end]

    else:
        ssmm -= lst[start]
        start +=1


print(answer)


