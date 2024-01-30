list_w_first=['WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW']
list_b_first=list_w_first[::-1]
min=65
M,N=map(int,input("").split(" "))
background=[]
for i in range(M):
    background.append(input(""))
for i in range(M-7):
    for j in range(N-7):
        b_count=0
        w_count=0
        for k in range(8):
            for l in range(8):
                if background[i+k][j+l] != list_w_first[k][l]:
                    w_count+=1
                if background[i+k][j+l] != list_b_first[k][l]:
                    b_count+=1
        if w_count<min:
            min=w_count
        if b_count<min:
            min=b_count

print(min) 