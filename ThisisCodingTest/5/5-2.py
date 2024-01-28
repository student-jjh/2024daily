from collections import deque

X = int(input())
for_check = [0 for i in range(30001)]

queue = deque()
queue.append(X)



while queue:

    now = queue.popleft()

    

    if now % 5 ==0 and for_check[now//5] ==0:
        temp = now // 5
        for_check[temp] = for_check[now] +1
        if temp == 1:
            break
        else:
            queue.append(temp)

    if now % 3 ==0 and for_check[now//3] ==0:
        temp = now // 3
        for_check[temp] = for_check[now] +1
        if temp == 1:
            break
        else:
            queue.append(temp)

    if now % 2 ==0 and for_check[now//2] ==0:
        temp = now // 2
        for_check[temp] = for_check[now] +1
        if temp == 1:
            break
        else:
            queue.append(temp)
    
    temp = now -1
    if for_check[now-1] == 0:
        for_check[temp] = for_check[now] +1
        if temp ==1:
            break

        else:
            queue.append(temp)
    
    
print(for_check[1])