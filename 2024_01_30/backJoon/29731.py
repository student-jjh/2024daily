temp_list = ['Never gonna give you up','Never gonna let you down','Never gonna run around and desert you','Never gonna make you cry','Never gonna say goodbye','Never gonna tell a lie and hurt you','Never gonna stop',]

N = int(input())
check = True
for _ in range(N):
    temp = input()
    if temp not in temp_list:
        print("No")
        check = False
        break

if check == True:
    print("Yes")
