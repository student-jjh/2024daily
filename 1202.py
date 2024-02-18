# 무게와 가격이 주어진 문제
# 최대 가격을 구하는 프로그램 + 가방 별로 담을 수 있는 무게가 있고, 가방당 하나의 보석만 담을 수 있음
# 아이디어는 일단 비싼거 부터 꺼내면서 가벼운 가방..?
# 힙큐를 쓰면.. 알아서 비싼건 골라주니.. 가방에 담을 수 있는거 다 고를까..?
import sys
import heapq # 힙
input=sys.stdin.readline # 입력 빠르게
# 보석 종류, 가방 종류
N,K = map(int,input().split())
# 보석 입력 0 = 무게, V 는 가격
gems = []
for _ in range(N):
    gems.append(tuple(map(int,input().split())))
# 가방 
bags = []
for _ in range(K):
    bags.append(int(input()))

# 보석 무게순 정렬
gems.sort()

# 가방 무게순 정렬
bags.sort()

result = 0

for_answer = []
for bag in bags:
    while gems and gems[0][0] <= bag:
       heapq.heappush(for_answer,-gems[0][1])
       heapq.heappop(gems)
    
    if for_answer:
        result -= heapq.heappop(for_answer)

print(result)