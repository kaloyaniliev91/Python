number_of_lines = int(input())
left_sum = 0
right_sum = 0

for i in range(0, number_of_lines * 2):
    numbers_for_left_side = float(input())
    left_sum += numbers_for_left_side

for i in range(1, number_of_lines):
    numbers_for_right_side = float(input())
    right_sum += numbers_for_right_side

diff = abs(left_sum - right_sum)

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    print(f'No, diff = {diff}')