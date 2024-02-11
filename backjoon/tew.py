N,M = map(int,input().split())

temp = list(map(int,input().split()))

temp.sort()
rs = []
log = set()

def recur(num):
    if num == M:
        if tuple(rs) not in log:
            print(*rs)
            log.add(tuple(rs))
        return
    
    for i in range(N):
        if rs == [] :
            rs.append(temp[i])
            recur(num+1)
            rs.pop()

        elif rs[-1] <= temp[i]:
            rs.append(temp[i])
            recur(num+1)
            rs.pop()

recur(0)