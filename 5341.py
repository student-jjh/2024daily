while True:
    N = int(input())

    if N == 0 :
        break

    answer = 0

    for i in range(1,N+1):
        answer+=i
    
    print(answer)