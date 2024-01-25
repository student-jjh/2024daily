from collections import deque
import sys
input = sys.stdin.readline



T = int(input().strip())

for i in range(1,T+1):
    stop = False
    temp_lst = []
    commends = input().strip()
    p = int(input().strip())
    exec("temp_lst = " + input().strip())
    queue = deque(temp_lst)
    cmd = 0

    for commend in commends:
        if commend == 'R':
            if cmd == 0 :
                cmd = 1
            else:
                cmd = 0
        else:
            if len(queue) == 0:
                print("error")
                stop = True
                break
            else:
                if cmd == 0:
                    queue.popleft()
                else:
                    queue.pop()
    if stop == True:
        continue
    if cmd == 0:
        print("[",end="")
        while queue:
            if len(queue) !=1:
                print(queue.popleft(),end=",")
            else:
                print(queue.popleft(),end="")
        print("]")
    else:
        print("[",end="")
        while queue:
            if len(queue) !=1:
                print(queue.pop(),end=",")
            else:
                print(queue.pop(),end="")
        print("]")

