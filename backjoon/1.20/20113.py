N = int(input())

temp_list = list(map(int,input().split()))

votes = [0 for _ in range(N+1)]

for vote in temp_list:
    if vote != 0:
        votes[vote] += 1
    
mx = max(votes)
if votes.count(mx) > 1:
    print("skipped")

else:
    print(votes.index(mx))