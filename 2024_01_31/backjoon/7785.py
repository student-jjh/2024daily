N = int(input())

company_dict = {}

for _ in range(N):
    name,come = map(str,input().split())

    company_dict[name] = come

temp = list(company_dict.items())

temp.sort(reverse=True)
for name in temp:
    if name[1] == "enter":
        print(name[0])