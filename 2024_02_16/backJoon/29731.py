temp =[
'Never gonna give you up',
'Never gonna let you down',
'Never gonna run around and desert you',
'Never gonna make you cry',
'Never gonna say goodbye',
'Never gonna tell a lie and hurt you',
'Never gonna stop',
]
N = int(input())
check = True

for _ in range(N):
    word = input()
    if word not in temp:
        check = False

if check :
    print("No")

else:
    print("Yes")