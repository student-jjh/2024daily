N = int(input())

def is_it(num):
    if num == 1:
        return False
    check = [False for _ in range(num+1)]
    for i in range(2,int(num**0.5)+1):
        if check[i] == False:
            for j in range(i,num+1,i):
                check[j] = True

    if check[num] == False:
        return True
    return False
lst = [2,3,5,7]
cnt = 0
def recur(num,lst):
    global cnt
    if num == N:
        for number in lst:
            if is_it(number) == True:
                print(number)
                cnt +=1
        return
    temp = []
    for i in lst:
        for j in range(1,10):
            if is_it(int(str(i)+str(j))):
                temp.append(int((str(i)+str(j))))
    temp.sort()
    recur(num+1,temp)

recur(1,lst)
