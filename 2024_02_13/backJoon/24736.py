
team_1 = list(map(int,input().split()))
team_2 = list(map(int,input().split()))
cal = [6,3,2,1,2]
score_1 = 0
score_2 = 0
for i in range(5):
    score_1+=team_1[i]*cal[i]
    score_2+=team_2[i]*cal[i]

print(f"{score_1} {score_2}")
