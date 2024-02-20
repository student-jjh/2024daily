X1,X2,X3 = map(int,input().split())
Y1,Y2,Y3 = map(int,input().split())

X= X1*3 + X2 * 20 + X3 * 120
Y = Y1 * 3 + Y2 * 20 + Y3 * 120

if X > Y:
    print("Max")
elif Y > X:
    print("Mel")
else:
    print("Draw")