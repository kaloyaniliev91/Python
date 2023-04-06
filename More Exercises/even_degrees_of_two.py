number = int(input())

for number in range (0, number + 1):

    if number % 2 != 0:
        continue

    print(2 ** number)