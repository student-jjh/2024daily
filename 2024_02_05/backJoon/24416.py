N = int(input())

call_fibo = [0 for _ in range(41)]
call_fibo[1] = 1
call_fibo[2] =1

for i in range(3,N+1):
    call_fibo[i] =call_fibo[i-1] +call_fibo[i-2]

print(call_fibo[N])
print(N-2)