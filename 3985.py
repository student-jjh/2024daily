L = int(input())
N = int(input())
cake_list = [0 for _ in range(L+1)]
expected = {}
real = {}

for j in range(1,N+1,1):
    P,K = map(int,input().split())

    expected[j] = ((K-P) +1)

    for c in range(P,K+1,1):
        if cake_list[c] == 0:
            cake_list[c] = j

for k in range(1,N+1,1):
    real[k] = cake_list.count(k)

expected = list(expected.items())
expected.sort(reverse = True)
expected.sort(key = lambda x: x[1] )
real = list(real.items())
real.sort(reverse = True)
real.sort(key = lambda x : x[1])

print(expected[-1][0])
print(real[-1][0])