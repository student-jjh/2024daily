N = int(input())

switch = list(map(int,input().split()))

students = int(input())

for _ in range(students):
    sex,number = map(int,input().split())
    # 남자면
    if sex == 1:
        for i in range(number-1,N,number):
            switch[i] = switch[i]^1
    # 여자면
    elif sex == 2:
        switch[number-1] ^= 1
        pi = number -1 + 1
        pj = number -1 - 1
        while True:
            if pi >= N or pj < 0 or switch[pi] != switch[pj]:
                break

            switch[pi] ^=1
            switch[pj] ^=1

            pi +=1
            pj -=1

for i in range(0,N,20):
    print(*switch[i:min(i+20,N)])

