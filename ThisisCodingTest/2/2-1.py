N = int(input())

move_list = map(str,input().split())

move_dic = {'R':[0,1],'L':[0,-1],'U':[-1,0],'D' :[1,0]}

x,y = (1,1)

for move in move_list:
    
    temp_x,temp_y = x,y

    temp_x += move_dic[move][0]
    temp_y += move_dic[move][1]

    if temp_x < 1 or temp_x >= N or temp_y <1 or temp_y <1:
        continue

    x,y = temp_x,temp_y


print(x,y)
    

