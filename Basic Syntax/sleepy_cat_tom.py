import math

days_off = int(input())

working_days = 365 - days_off

NORM_FOR_PLAY = 30_000

mins_play_per_day_when_working = 63
mins_play_per_day_when_dayoff = 127

total_mins_play = (365 - days_off) * 63 + (days_off * 127)

difference = abs(total_mins_play - NORM_FOR_PLAY)
hours = difference // 60
minutes = difference % 60

if total_mins_play > NORM_FOR_PLAY:
    print('Tom will run away')
    print(f'{hours} hours and {minutes} minutes more for play')
else:
    print('Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')