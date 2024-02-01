from collections import deque
N,K =map(int,input().split())
if N == K:
    print(0)
    exit(0)
for_count = [0 for _ in range(120000)]
queue = deque()
queue.append(N)
for_count[N] = 1
while queue:
    now = queue.popleft()
    break_check = False
    for item in (now+1,now-1,now*2):
        if item == K:
            print(for_count[now])
            break_check = True
            break

        elif 0< item < 120000 and for_count[item] ==0:
            for_count[item] = for_count[now] +1
            queue.append(item)
    if break_check == True:
        break



