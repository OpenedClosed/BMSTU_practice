number = input()
answer = 0
while (number != ''):
    if int(number) % 2 == 0:
        answer += int(number)
    number = input()
print(answer)