import sys

n = int(input())
max_num = -sys.maxsize

while n != 'Stop':
    num = int(input())

    if num > max_num:
        max_num = num

    input = input()


print(max_num)