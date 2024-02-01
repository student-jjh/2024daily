from collections import deque

A,B = map(int,input().split())
if len(str(A)) > len(str(B)):
    print(-1)


else:
    queue = deque()
    queue.append((A,1))
    break_point =False
    while queue:
        now,count = queue.popleft()

        if now * 2 == B:
            print(count +1)
            break_point =True
            break

        elif now *2 < B:
            queue.append((now*2,count +1))

        if str(now) + "1" == str(B):
            print(count +1)
            break_point = True
            break

        elif len(str(now) + "1") <= len(str(B)):
            queue.append((int(str(now)+"1"),count+1))
if break_point == False:
    print(-1)
