total_space = int(input()) * int(input()) * int(input())
space_fieled = 0

while space_fieled < total_space:
    box = input()

    if box == 'Done':
        print(f'{total_space - space_fieled} Cubic meters left.')
        break

    space_fieled += int(box)
else:
    print(f'No more free space! You need {space_fieled - total_space} Cubic meters more.')