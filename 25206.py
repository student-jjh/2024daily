grade_dic = {'A+' :	4.5,'A0' :	4.0,'B+' :	3.5,'B0' :	3.0,'C+' :	2.5,'C0' :	2.0,'D+' :	1.5,'D0' :	1.0,'F' :	0.0}

grade_sum = 0
how_cnt = 0

for i in range(20):
    temp = input().split()

    if temp[-1] != "P":
        how_cnt += float(temp[1])
        grade_sum += (float(temp[1]) * grade_dic[temp[-1]])

print(grade_sum / how_cnt)