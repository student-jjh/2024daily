N,A,B = map(int,input().split())

if A < B :
    print("Bus")

elif B == A:
    if N <=B:
        print("Anything")

    else:
        print("Bus")

else:
    if N <= B:
        print("Subway")

    else:
        print("Bus")