N = int(input())
N = N %1500000
if N == 0 :
    print(0)
elif N <=2:
    print(1)

else:
    a=1
    b =1
    for i in range(3,N+1):
        a,b = b,((a+b) % 1000000)

    print(b)
