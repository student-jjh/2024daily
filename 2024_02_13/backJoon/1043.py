N,M = map(int,input().split())

parent = [i for i in range(N+1)]

def find_all(X):
    if parent[X] != X:
        parent[X] = find_all(parent[X])

    return parent[X]

def union(A,B):
    A = find_all(A)
    B = find_all(B)

    if A == B:
        return
    elif A > B:
        parent[A] = B
    else:
        parent[B] = A


true_list = list(map(int,input().split()))
real_num = true_list[0]
true_list = true_list[1:]
for_check = set(true_list)
if for_check == set():
    answer = M
else:
    for i in range(real_num):
        parent[true_list[i]] = 0

for_answer = []
for i in range(M):
    temp = list(map(int,input().split()))
    if temp[0] >=2:
        temps = temp[1:]
        for i in range(len(temps)-1):
            union(temps[i],temps[i+1])

    for_answer.append(temp[1:])
cnt = 0

def find_not(lst):
    for i in lst:
        if find_all(i) == 0:
            return False
    return True
for i in range(M):
    if find_not(for_answer[i]) == True:
        cnt +=1

print(cnt)

