from collections import deque

N = int(input())

temp = list(map(int,input().split()))
temp = temp[::-1]

card = [i for i in range(N,0,-1)]
answer = deque()
for skill in temp:
    if skill == 1:
        answer.appendleft(card.pop())

    elif skill == 2:
        answer.insert(1,card.pop())
    else:
        answer.append((card.pop()))

print(*list(answer))