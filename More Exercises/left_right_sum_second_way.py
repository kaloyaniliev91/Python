number = int(input())

left_sum = 0
right_sum = 0

for i in range(2 * number):
    num = int(input())

    if i < number:
        left_sum += num
    else:
        right_sum += num

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    print(f'No, diff = {abs(left_sum - right_sum)}')