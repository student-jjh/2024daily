answer = 0

while True:
    try:
        gum_gum = input()
        answer += 1
    except EOFError:
        break

print(answer)