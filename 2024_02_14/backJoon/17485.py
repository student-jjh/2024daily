N = int(input())

def ara(n):
    a = [False,False] + [True]*(n-1)
    primes=[]

    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    return a

array_for_answer=ara(10001)
temp = []
for i in range(10001):
    if array_for_answer[i] == True:
        temp.append(i)

def is_it(num):
    if num == 1:
        return False
    for i in range(len(temp)):
        if int(num**0.5) < temp[i]:
             break
        if num % temp[i] ==0:
            return False
    return True

cnt = 0
lst = [2,3,5,7]
def recur(num,number):
    global cnt
    if num == N:
        print(number)

    for i in range(1,10):
        print(i)
        if is_it(int(str(number)+str(i))):
            recur(num+1,int(str(number)+str(i)))
recur(0,"")