N,r,c = map(int,input().split())

real_num = 2**N

def Z(real_num,i,j):

    if real_num == 1:
        return 1

    for_check = real_num // 2
    answer = 0
    if 0<= i < for_check and 0 <=j <for_check:
        answer += Z(for_check,i,j)
    if for_check<= j < real_num and 0 <=i <for_check:
        answer += for_check ** 2 + Z(for_check,i,j-for_check)
    if for_check<= i < real_num  and 0 <=j <for_check:
        answer += 2*(for_check ** 2) + Z(for_check, i-for_check, j)
    if for_check<= i < real_num and for_check<= j < real_num:
        answer += 3*(for_check ** 2) + Z(for_check, i-for_check, j-for_check)

    return answer

print(Z(real_num,r,c)-1)