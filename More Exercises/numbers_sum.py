numbers_count = int(input())

numbers_sum = 0

for i in range(1, numbers_count + 1):
    current_num = int(input())
    numbers_sum = numbers_sum + current_num

print(str(numbers_sum))