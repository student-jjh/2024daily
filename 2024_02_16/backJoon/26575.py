
N = int(input())
for _ in range(N):
    total = 0
    num_dogs, food_per_dog, pound_per_food= map(float, input().split())
    total = num_dogs*food_per_dog*pound_per_food

    print(f'${total:.2f}')