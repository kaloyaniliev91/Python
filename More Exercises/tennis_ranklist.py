from math import floor

tournaments = int(input())
starting_points = int(input())

gained_points = 0
won_tournaments = 0

for _ in range(tournaments):
    result = input()

    if result == 'W':
        won_tournaments += 1
        gained_points += 2000
    elif result == 'F':
        gained_points += 1200
    elif result == 'SF':
        gained_points += 720

all_points = starting_points + gained_points

print(f'Final points: {floor(all_points)}')
print(f'Average points: {floor(gained_points / tournaments)}')
print(f'{(won_tournaments / tournaments) * 100:.2f}%')