T = int(input())

def cal_dif(a,b):
    cnt =0
    for i in range(4):
        if a[i] != b[i]:
            cnt +=1
    return cnt

for i in range(T):
    N  = int(input())
    if N <= 8:
        temp  = list(map(str,input().split()))
        line = []
        for item in temp:
            teemmpp = list(item)
            line.append(teemmpp)

        line.sort()
        mx = 1000000000
        for i in range(N-2):
            for j in range(i+1,N-1):
                for k in range(j+1,N):
                    temp = 0
                    temp += cal_dif(line[i],line[j])
                    temp += cal_dif(line[k], line[j])
                    temp += cal_dif(line[i], line[k])

                    mx = min(mx,temp)
        print(mx)
    else:
        temp = list(map(str, input().split()))
        dic = {}
        for item in temp:
            if item in dic:
                dic[item]+=1
            else:
                dic[item] =1

        if max(list(dic.values())) >=3:
            print(0)

        else:
            line = []
            for item in temp:
                teemmpp = list(item)
                line.append(teemmpp)

            line.sort()
            mx = 1000000000
            for i in range(N - 2):
                for j in range(i + 1, N - 1):
                    for k in range(j + 1, N):
                        temp = 0
                        temp += cal_dif(line[i], line[j])
                        temp += cal_dif(line[k], line[j])
                        temp += cal_dif(line[i], line[k])

                        mx = min(mx, temp)
            print(mx)

