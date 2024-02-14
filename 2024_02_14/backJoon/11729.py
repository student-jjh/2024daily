def hanoi(n,a,b,c):
    if n==1:
        print(a,c)
    else:
        hanoi(n-1,a,c,b)
        print(a,c)
        hanoi(n-1,b,a,c)

def hanoi_count(n):
    if n==1:
        return 1
    else:
        return hanoi_count(n-1)*2+1

n=int(input())
print(hanoi_count(n))
hanoi(n,1,2,3)