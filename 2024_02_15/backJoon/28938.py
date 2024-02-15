N = int(input())

temp_lst = list(map(int,input().split()))
temp = sum(temp_lst)
if temp > 0 :
    print("Right")
elif temp < 0 :
    print("Left")
else:
    print("Stay")